from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from submit_indexnow import (
    DEFAULT_INDEXNOW_ENDPOINT,
    extract_urls_from_sitemap,
    load_yaml,
    submit_to_indexnow,
)


class SubmitIndexNowTests(unittest.TestCase):
    def test_extract_urls_from_sitemap(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            sitemap = Path(tmp_dir) / "sitemap.xml"
            sitemap.write_text(
                """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://example.com/</loc></url>
  <url><loc>https://example.com/about.html</loc></url>
</urlset>""",
                encoding="utf-8",
            )
            urls = extract_urls_from_sitemap(sitemap)
            self.assertEqual(urls, ["https://example.com/", "https://example.com/about.html"])

    def test_dry_run(self):
        success, code, msg = submit_to_indexnow(
            host="example.com",
            key="1234567890abcdef",
            urls=["https://example.com/"],
            dry_run=True,
        )
        self.assertTrue(success)
        self.assertEqual(code, 200)
        self.assertIn("[DRY RUN]", msg)

    def test_invalid_key(self):
        with self.assertRaises(ValueError):
            submit_to_indexnow(
                host="example.com",
                key="short",
                urls=["https://example.com/"],
            )

    @patch("urllib.request.urlopen")
    def test_successful_submission(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_response.read.return_value = b'{"success": true}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        success, code, msg = submit_to_indexnow(
            host="iptc.pages.dev",
            key="DC4AB582C527A7A168FC391B84B8995E",
            urls=["https://iptc.pages.dev/about.html"],
        )
        self.assertTrue(success)
        self.assertEqual(code, 200)
        self.assertIn("HTTP 200", msg)


if __name__ == "__main__":
    unittest.main()
