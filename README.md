# ShortLink-Bypass

A lightweight Python tool for resolving shortened URLs, decoding Base64 links, following HTTP redirects, and extracting some hidden destination URLs.

**Repository:** https://github.com/Cracka564/ShortLink-Bypass

## Features

- Extract destination URLs from common query parameters (`url`, `u`, `link`, `target`, `dest`, `redirect`)
- Decode Base64-encoded destination URLs
- Follow common HTTP redirects
- Detect some meta-refresh and JavaScript redirect patterns
- Look for Base64-encoded URLs in page content

## Install on Termux (Android)

### 1. Update Termux

```bash
pkg update && pkg upgrade -y
```

### 2. Install Python and Git

```bash
pkg install python git -y
```

### 3. Download the repository

```bash
git clone https://github.com/Cracka564/ShortLink-Bypass.git
cd ShortLink-Bypass
```

### 4. Install the required Python package

```bash
python -m pip install requests
```

### 5. Check the files

```bash
ls
```

Make sure the Python script `bypass.py` is present.

### 6. Run the tool

```bash
python bypass.py "https://example.com/short-link"
```

Replace `https://example.com/short-link` with a short URL you are allowed to inspect. The tool prints the destination URL it extracts or resolves.

## Run it again later

Open Termux and enter:

```bash
cd ~/ShortLink-Bypass
python bypass.py "https://example.com/short-link"
```

## Update the repository

From inside the project folder, run:

```bash
cd ~/ShortLink-Bypass
git pull
```

## Requirements

- Android with Termux
- Python 3
- Git
- Python package: `requests`

## Troubleshooting

**`No such file or directory: bypass.py`**

Run `ls` to check the actual script filename. If the repository uses a different filename, replace `bypass.py` in the run command with that filename.

**`ModuleNotFoundError: No module named 'requests'`**

Run:

```bash
python -m pip install requests
```

## Safety and limitations

- This tool attempts to resolve URLs; it does not download files.
- Some websites use CAPTCHA, login, JavaScript challenges, or other protections that this script does not handle.
- Check the destination before opening it. Short links can lead to unsafe websites.
- Use the tool responsibly and follow the target website's terms.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
