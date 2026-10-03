#!/usr/bin/env python3
import sys
import base64
import re
import requests
from urllib.parse import urlparse, parse_qs, unquote

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}

def try_base64_decode(text):
    text = text.strip()
    # pad if needed
    missing = len(text) % 4
    if missing:
        text += "=" * (4 - missing)
    try:
        decoded = base64.b64decode(text).decode("utf-8", errors="ignore")
        if decoded.startswith("http"):
            return decoded
    except Exception:
        pass
    return None

def extract_from_query(url):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    for key in ["url", "u", "link", "target", "dest", "redirect"]:
        if key in qs:
            val = qs[key][0]
            # try raw
            if val.startswith("http"):
                return unquote(val)
            # try base64
            decoded = try_base64_decode(val)
            if decoded:
                return decoded
    return None

def follow_redirects(url, max_hops=15):
    session = requests.Session()
    session.headers.update(HEADERS)
    current = url
    seen = set()

    for _ in range(max_hops):
        if current in seen:
            break
        seen.add(current)

        try:
            r = session.get(current, allow_redirects=False, timeout=12)
        except Exception as e:
            return current, f"error: {e}"

        # redirect
        if r.status_code in (301, 302, 303, 307, 308):
            loc = r.headers.get("Location")
            if not loc:
                break
            if loc.startswith("/"):
                parsed = urlparse(current)
                loc = f"{parsed.scheme}://{parsed.netloc}{loc}"
            current = loc
            continue

        # no more redirects → check page for hidden target
        text = r.text

        # meta refresh
        m = re.search(r'url=["\']?(https?://[^"\'>\s]+)', text, re.I)
        if m:
            current = m.group(1)
            continue

        # common js / data-url patterns
        m = re.search(r'(?:window\.location|location\.href|data-url|data-href)\s*=\s*["\'](https?://[^"\']+)', text, re.I)
        if m:
            current = m.group(1)
            continue

        # base64 hidden in page
        for match in re.finditer(r'[A-Za-z0-9+/=]{20,}', text):
            decoded = try_base64_decode(match.group(0))
            if decoded and "http" in decoded:
                current = decoded
                break
        else:
            break  # nothing found

    return current, "ok"

def bypass(url):
    # 1. try extract from query params (works on vipshort style)
    direct = extract_from_query(url)
    if direct:
        return direct

    # 2. normal redirect follow + page scrape
    final, status = follow_redirects(url)
    return final

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python bypass.py <short-url>")
        sys.exit(1)

    short = sys.argv[1]
    result = bypass(short)
    print(result)
