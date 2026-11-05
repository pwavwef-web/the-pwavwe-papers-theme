"""Check the theme before uploading it to Blogger.

    python scripts/check-theme.py          # local checks only
    python scripts/check-theme.py --live   # also check the live site and assets

Local checks: the theme is well-formed XML, the head's JSON-LD is valid JSON,
every inline script in the theme and the page files parses (needs Node.js),
and every asset the theme loads from GitHub exists in assets/.

--live adds: each GitHub asset URL answers 200, and the live site's
pwavwe-theme-version matches the local one, so you can tell whether the
local theme has been uploaded yet.

Exits 1 if any check fails.
"""

import json
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEME = ROOT / "pwavwe-papers-editorial-theme.xml"
SITE = "https://blogs.pwavwe.com/"
ASSET_URL = re.compile(r"https://raw\.githubusercontent\.com/[\w.-]+/[\w.-]+/main/(assets/[\w./-]+)")
VERSION = re.compile(r"<meta content='([^']+)' name='pwavwe-theme-version'/>")
failures = []


def check(ok, message):
    print(("ok    " if ok else "FAIL  ") + message)
    if not ok:
        failures.append(message)


def fetch(url, method="GET"):
    request = urllib.request.Request(url, method=method, headers={"User-Agent": "pwavwe-theme-check"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.status, response.read().decode("utf-8", "replace") if method == "GET" else ""


def check_scripts(name, scripts):
    node = shutil.which("node")
    if not node:
        print(f"skip  {name}: Node.js not found, scripts not parsed")
        return
    for i, code in enumerate(scripts, 1):
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f:
            f.write(code)
        result = subprocess.run([node, "--check", f.name], capture_output=True, text=True)
        Path(f.name).unlink()
        check(result.returncode == 0, f"{name}: script {i} parses" +
              ("" if result.returncode == 0 else "\n" + result.stderr.strip()))


def main():
    live = "--live" in sys.argv[1:]
    text = THEME.read_text(encoding="utf-8")

    try:
        ET.fromstring(text.encode("utf-8"))
        check(True, "theme is well-formed XML")
    except ET.ParseError as error:
        check(False, f"theme is well-formed XML ({error})")

    for block in re.findall(r"<script type='application/ld\+json'>(.*?)</script>", text, re.S):
        try:
            json.loads(block)
            check(True, "head JSON-LD is valid JSON")
        except ValueError as error:
            check(False, f"head JSON-LD is valid JSON ({error})")

    check_scripts("theme", re.findall(r"<script[^>]*>\s*//<!\[CDATA\[(.*?)//\]\]>", text, re.S))
    for page in sorted(ROOT.glob("*-page.html")):
        html = re.sub(r"<!--.*?-->", "", page.read_text(encoding="utf-8"), flags=re.S)
        check_scripts(page.name, re.findall(r"<script>(.*?)</script>", html, re.S))

    assets = sorted(set(ASSET_URL.findall(text)))
    for asset in assets:
        check((ROOT / asset).is_file(), f"{asset} exists locally")

    version = VERSION.search(text)
    check(bool(version), "theme has a pwavwe-theme-version stamp")

    if live:
        for asset in assets:
            url = next(m.group(0) for m in ASSET_URL.finditer(text) if m.group(1) == asset)
            try:
                status = fetch(url, "HEAD")[0]
            except Exception as error:
                status = error
            check(status == 200, f"{url} answers 200 (got {status})")
        try:
            page = fetch(SITE)[1]
            found = re.search(r"<meta content='([^']+)' name='pwavwe-theme-version'", page)
            live_version = found.group(1) if found else "none (older than the stamp)"
        except Exception as error:
            live_version = f"unreachable ({error})"
        local_version = version.group(1) if version else "none"
        print(f"info  live theme version: {live_version}; local: {local_version}")
        if live_version != local_version:
            print("info  the local theme is not the one installed on the live site")

    print(f"\n{len(failures)} check(s) failed." if failures else "\nAll checks passed.")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
