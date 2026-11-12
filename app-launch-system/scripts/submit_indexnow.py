#!/usr/bin/env python3
"""Submit URLs or sitemap to the IndexNow protocol endpoints (Bing, Yandex, etc.)."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
import xml.etree.ElementTree as ET

try:
    import yaml
except ImportError:
    yaml = None


DEFAULT_INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
INDEX_NOW_KEY_PATTERN = re.compile(r"^[A-Za-z0-9_-]{8,128}$")
BATCH_SIZE = 10000


def load_yaml(path: Path) -> dict:
    if yaml is not None:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            return data if isinstance(data, dict) else {}
    text = path.read_text(encoding="utf-8")
    result: dict = {}
    host_match = re.search(r'(?m)^websiteUrl:\s*["\']?(https?://[^"\'\s]+)', text)
    if host_match:
        result["websiteUrl"] = host_match.group(1)
    key_match = re.search(r'(?m)^\s*indexNowKey:\s*["\']?([A-Za-z0-9_-]+)', text)
    if key_match:
        result.setdefault("bing", {})["indexNowKey"] = key_match.group(1)
    return result


def extract_urls_from_sitemap(sitemap_path: Path) -> list[str]:
    """Extract all <loc> URLs from a sitemap XML file."""
    if not sitemap_path.is_file():
        raise FileNotFoundError(f"Sitemap file not found: {sitemap_path}")
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls: list[str] = []
    namespaces = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = root.findall(".//sm:loc", namespaces) or root.findall(".//loc")
    for loc in locs:
        if loc.text and loc.text.strip():
            urls.append(loc.text.strip())
    return urls


def submit_to_indexnow(
    host: str,
    key: str,
    urls: list[str],
    key_location: str | None = None,
    endpoint: str = DEFAULT_INDEXNOW_ENDPOINT,
    user_agent: str = "Mozilla/5.0 (compatible; IndexNowSubmitter/1.0)",
    dry_run: bool = False,
) -> tuple[bool, int, str]:
    """Submit a list of URLs to an IndexNow API endpoint.

    Returns (success, http_status_code, response_message).
    """
    if not host:
        raise ValueError("Host is required (e.g. example.com or iptc.pages.dev)")
    if not key or not INDEX_NOW_KEY_PATTERN.fullmatch(key):
        raise ValueError("Invalid IndexNow key. Must be 8-128 alphanumeric characters, hyphens or underscores.")
    if not urls:
        raise ValueError("No URLs provided for submission.")

    parsed_host = urllib.parse.urlparse(host if "://" in host else f"https://{host}").netloc or host
    if not key_location:
        key_location = f"https://{parsed_host}/{key}.txt"

    payload = {
        "host": parsed_host,
        "key": key,
        "keyLocation": key_location,
        "urlList": urls,
    }

    if dry_run:
        return True, 200, f"[DRY RUN] Would submit {len(urls)} URLs for host {parsed_host} to {endpoint}"

    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        endpoint,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": user_agent,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            status_code = response.status
            body = response.read().decode("utf-8", errors="replace")
            msg = f"HTTP {status_code}: URLs submitted successfully to {endpoint}"
            if body:
                msg += f" - Response: {body}"
            return True, status_code, msg
    except urllib.error.HTTPError as exc:
        status_code = exc.code
        body = exc.read().decode("utf-8", errors="replace")
        status_reasons = {
            400: "Invalid format / bad request",
            403: "Key not found or key location mismatch (ensure <key>.txt is live on the site)",
            422: "Unprocessable entity (URLs don't match host or key issue)",
            429: "Too many requests",
        }
        reason = status_reasons.get(status_code, "HTTP Error")
        return False, status_code, f"Failed with HTTP {status_code} ({reason}): {body}"
    except Exception as exc:
        return False, 0, f"Network error submitting to {endpoint}: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-info", type=Path, help="Path to app-info.yaml")
    parser.add_argument("--sitemap", type=Path, help="Path to sitemap.xml to extract all URLs from")
    parser.add_argument("--url", action="append", dest="urls", help="Specific URL to submit (can specify multiple)")
    parser.add_argument("--key", type=str, help="IndexNow key (defaults to bing.indexNowKey in app-info.yaml)")
    parser.add_argument("--host", type=str, help="Host name (e.g. iptc.pages.dev, defaults to websiteUrl in app-info)")
    parser.add_argument("--key-location", type=str, help="Full URL to key file (defaults to https://<host>/<key>.txt)")
    parser.add_argument("--endpoint", type=str, default=DEFAULT_INDEXNOW_ENDPOINT, help=f"IndexNow endpoint (default: {DEFAULT_INDEXNOW_ENDPOINT})")
    parser.add_argument("--dry-run", action="store_true", help="Simulate submission without making HTTP request")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of URLs to submit")

    args = parser.parse_args()

    app_info_path = args.app_info
    if not app_info_path:
        candidates = [
            Path("app-info.yaml"),
            Path(__file__).resolve().parents[2] / "app-info.yaml",
            Path(__file__).resolve().parent.parent / "config" / "app-info.yaml",
        ]
        for candidate in candidates:
            if candidate.is_file():
                app_info_path = candidate
                break

    key = args.key
    host = args.host
    website_url = None

    if app_info_path and app_info_path.is_file():
        app_data = load_yaml(app_info_path)
        if not key:
            key = (app_data.get("bing") or {}).get("indexNowKey")
        if not host:
            website_url = app_data.get("websiteUrl")
            if website_url:
                host = urllib.parse.urlparse(website_url).netloc

    if not key:
        print("ERROR: IndexNow key is required. Specify via --key or in app-info.yaml (bing.indexNowKey).", file=sys.stderr)
        return 1

    if not host:
        print("ERROR: Host is required. Specify via --host or in app-info.yaml (websiteUrl).", file=sys.stderr)
        return 1

    urls_to_submit: list[str] = []
    if args.urls:
        urls_to_submit.extend(args.urls)

    sitemap_path = args.sitemap
    if not sitemap_path and not urls_to_submit:
        sitemap_candidates = [
            Path("sitemap.xml"),
            Path(__file__).resolve().parents[2] / "sitemap.xml",
        ]
        if app_info_path:
            sitemap_candidates.append(app_info_path.parent / "sitemap.xml")
        for sc in sitemap_candidates:
            if sc.is_file():
                sitemap_path = sc
                break

    if sitemap_path:
        print(f"Reading URLs from sitemap: {sitemap_path}")
        sitemap_urls = extract_urls_from_sitemap(sitemap_path)
        print(f"Found {len(sitemap_urls)} URLs in sitemap.")
        urls_to_submit.extend(sitemap_urls)

    seen = set()
    unique_urls = []
    for u in urls_to_submit:
        if u not in seen:
            seen.add(u)
            unique_urls.append(u)
    urls_to_submit = unique_urls

    if args.limit and args.limit > 0:
        urls_to_submit = urls_to_submit[:args.limit]

    if not urls_to_submit:
        print("ERROR: No URLs to submit. Provide --sitemap or --url.", file=sys.stderr)
        return 1

    print(f"Submitting {len(urls_to_submit)} URLs for host: {host}")
    print(f"IndexNow Key: {key}")
    key_loc = args.key_location or f"https://{host}/{key}.txt"
    print(f"Key Location: {key_loc}")
    print(f"Endpoint: {args.endpoint}")

    all_success = True
    for i in range(0, len(urls_to_submit), BATCH_SIZE):
        batch = urls_to_submit[i : i + BATCH_SIZE]
        success, code, msg = submit_to_indexnow(
            host=host,
            key=key,
            urls=batch,
            key_location=key_loc,
            endpoint=args.endpoint,
            dry_run=args.dry_run,
        )
        print(f"[{i+1}-{i+len(batch)}] {msg}")
        if not success:
            all_success = False

    return 0 if all_success else 1


if __name__ == "__main__":
    raise SystemExit(main())
