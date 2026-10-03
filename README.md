ShortLink-Bypass

A lightweight Python tool to resolve shortened URLs, decode Base64 links, follow HTTP redirects, and extract hidden destination URLs.

Features

- Extract destination URLs from common query parameters.
- Decode Base64-encoded URLs.
- Follow common HTTP redirects.
- Detect meta-refresh and JavaScript redirect patterns.
- Scan page content for Base64-encoded URLs.

Requirements

- Python 3.8+
- requests

Installation

git clone https://github.com/Cracka564/ShortLink-Bypass.git
cd ShortLink-Bypass
pip install requests

Usage

python bypass.py "https://example.com/short-link"

The tool prints the extracted or resolved URL.

Example

python bypass.py "https://example.com/?url=aHR0cHM6Ly9leGFtcGxlLmNvbQ=="


Notes

- This tool attempts to resolve URLs; it does not download files.
- Some websites use CAPTCHA, authentication, or other protections that this script does not handle.
- Always check the destination URL before opening it.
- Use this tool responsibly and follow the target website's terms.

