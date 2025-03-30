# m-put (Mass-PUT)

**m-put** is a simple bot designed to detect HTTP PUT vulnerabilities that allow unauthorized file uploads. This tool attempts to upload a test file and verify if it is accessible.

## 🎯 Features
- **Automatically detects enabled HTTP PUT**.
- **Verifies file uploads** to confirm exploitability.
- **Automatic cleanup**, attempts to delete the test file after verification.
- **Colorful output!** Uses Colorama for better readability.
- **Timeout handling**: If a website does not respond within 10 seconds, it is skipped.
- **Automatic result storage**:
  - `results.txt` for vulnerable websites.
  - `failed.txt` for websites that failed the test or encountered errors.
- **Prevents errors on Ctrl+C**, allowing safe interruption.

## 📦 Installation
Make sure you have Python 3 and pip installed. Then install dependencies:

```sh
pip install -r requirements.txt
```

Or manually:

```sh
pip install requests colorama
```

## 🚀 Usage
1. Create a `list.txt` file and add target URLs, one per line:
   ```txt
   example.com
   https://vulnerable-site.com
   http://192.168.1.1
   ```
2. Run `m-put.py`:
   ```sh
   python3 m-put.py
   ```

## 📝 Scan Results
After execution, results will be stored in:
- **`results.txt`** → Contains vulnerable URLs.
- **`failed.txt`** → Contains URLs that failed the test.

## ⚠️ Disclaimer
This tool is for educational and legal security testing purposes only. Do not use it on systems without permission!

---

Made with ❤️ by will and crew

