"""公开边界与人工修改保护的回归检查。"""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'site'))
spec = importlib.util.spec_from_file_location('official', ROOT/'app-launch-system/scripts/build_official_site.py')
official = importlib.util.module_from_spec(spec)
spec.loader.exec_module(official)
from validate_public import check


class OfficialSiteTests(unittest.TestCase):
    def test_worker_denies_internal_and_encoded_paths(self):
        node = shutil.which('node')
        if not node: self.skipTest('Node 未安装')
        with tempfile.TemporaryDirectory() as temp:
            worker = Path(temp)/'worker.mjs'
            worker.write_text(official.worker(['index.html','en-US/index.html','assets/icon.png','ja-JP/features/一括/index.html']),encoding='utf-8')
            runner = Path(temp)/'check.mjs'
            runner.write_text('''import worker from './worker.mjs';
const env = {ASSETS: {fetch: async () => new Response('public')}};
for (const [path, expected] of [['/',200],['/en-US/',200],['/en-US',200],['/assets/icon.png',200],['/ja-JP/features/%E4%B8%80%E6%8B%AC/',200],['/app-info.yaml',404],['/analysis-evidence.json',404],['/app-launch-system/scripts/launch.py',404],['/site/content.py',404],['/.site-audit/project-facts.json',404],['/%61pp-info.yaml',404],['/%ZZ',400]]) {
 const response = await worker.fetch(new Request('https://iptc.pages.dev'+path), env);
 if (response.status !== expected) throw new Error(path+': '+response.status);
}
''',encoding='utf-8')
            subprocess.run([node,str(runner)],check=True,capture_output=True)

    def test_private_file_and_missing_anchor_fail_validation(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            (root/'index.html').write_text('<a href="#missing">Jump</a>',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'锚点'): check(root)
            (root/'index.html').write_text('<main id="main">Public</main>',encoding='utf-8')
            (root/'app-info.yaml').write_text('internal: true',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'内部文件'): check(root)

    def test_rebuild_preserves_unknown_and_modified_public_files(self):
        for changed in (False, True):
            with self.subTest(modified=changed), tempfile.TemporaryDirectory() as temp:
                root=Path(temp); public=root/'public'; public.mkdir(); audit=root/'.site-audit';audit.mkdir()
                target=public/'index.html'; target.write_text('manual change',encoding='utf-8')
                if changed:
                    (audit/'generation-manifest.json').write_text(json.dumps({'files':[{'path':'index.html','sha256':'previous-hash'}]}),encoding='utf-8')
                with patch.object(official,'ROOT',root), patch.object(official,'AUDIT',audit):
                    with self.assertRaisesRegex(RuntimeError,'人工作业'): official.build()
                self.assertEqual(target.read_text(encoding='utf-8'),'manual change')


if __name__ == '__main__': unittest.main()
