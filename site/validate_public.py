"""构建时检查可发布目录，失败时保留已有产物。"""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.refs, self.ids, self.schemas = [], set(), []
        self.schema = False
        self.buffer = ''
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        for key in ('href', 'src', 'poster'):
            if key in attrs: self.refs.append(attrs[key])
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.schema = True
            self.buffer = ''

    def handle_data(self, data):
        if self.schema: self.buffer += data

    def handle_endtag(self, tag):
        if tag == 'script' and self.schema:
            self.schemas.append(json.loads(self.buffer))
            self.schema = False


def check(root):
    root = Path(root).resolve()
    errors = []
    pages = {}
    for path in root.rglob('*'):
        if not path.is_file(): continue
        rel = path.relative_to(root)
        if any(p.startswith('.') or p in {'content','aso','seo-geo','app-launch-system','__pycache__'} for p in rel.parts) or path.suffix in {'.yaml','.yml','.py','.md','.key','.pem','.keystore'} or path.name.endswith('manifest.json'):
            errors.append(f'内部文件进入公开目录：{rel}')
        if path.suffix in {'.json','.webmanifest'}: json.loads(path.read_text(encoding='utf-8'))
        if path.suffix == '.html':
            text=path.read_text(encoding='utf-8')
            if any(token in text for token in ['feature-evidence','core/core_','C:\\work\\','{{','\ufffd','youtube-poster.jpg']):
                errors.append(f'内部证据、错误封面或未替换内容：{rel}')
            pages[path] = Page(text)
    for path,page in pages.items():
        for ref in page.refs:
            url=urlsplit(ref)
            if url.scheme or url.netloc: continue
            target=(root/unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent/unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(root):
                errors.append(f'路径越界：{ref}');continue
            if target.is_dir(): target=target/'index.html'
            elif not target.exists() and not target.suffix: target=target.with_suffix('.html')
            if not target.is_file(): errors.append(f'{path.relative_to(root)} 缺少 {ref}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(root)} 缺少锚点 {ref}')
    if errors: raise ValueError('\n'.join(errors[:30]))
    return {'passed':True,'htmlPages':len(pages)}
