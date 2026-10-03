# ShortLink-Bypass

A lightweight Python tool for resolving shortened URLs, decoding Base64 links, following HTTP redirects, and extracting some hidden destination URLs.

## Features

- Extract URLs from common query parameters (`url`, `u`, `link`, `target`, `dest`, `redirect`)
- Decode Base64-encoded destination URLs
- Follow common HTTP redirects
- Detect some meta-refresh and JavaScript redirect patterns
- Look for Base64-encoded URLs in page content

## Install on Termux (Android)

### 1. Update Termux packages

```bash
pkg update && pkg upgrade -y
```

### 2. Install Python and Git

```bash
pkg install python git -y
```

### 3. Clone this repository

Replace `YOUR-USERNAME` with your GitHub username:

```bash
git clone https://github.com/Cracka564/ShortLink-Bypass.git


```bash
cd ShortLink-Bypass
```

### 4. Install the Python dependency

```bash
python -m pip install requests
```

### 5. Run the tool

If the script is named `bypass.py`:

```bash
python bypass.py "https://example.com/short-link"
```

The tool prints the extracted or resolved URL.

## Update the project

From inside the project folder:

```bash
git pull
```

## Requirements

- Android with Termux
- Python 3
- Git
- `requests`

## Notes

- This tool resolves URLs; it does not download files.
- Some sites use CAPTCHA, login, JavaScript challenges, or other protections that this script does not handle.
- Check a destination URL before opening it. Short links can lead to unsafe websites.
- Use the tool responsibly and follow the target website's terms.

## License

This project is licensed under the MIT License.
See the [LICENSE](https://github.com/Cracka564/ShortLink-Bypass/blob/main/LICENSE) file for details.
