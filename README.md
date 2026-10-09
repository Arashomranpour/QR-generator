<div align="center">

# 🔳 QR Code Generator

**Turn any text or link into a QR code - saved as both PNG and SVG - from a tiny command-line tool.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![pyqrcode](https://img.shields.io/badge/pyqrcode-QR-informational)
![Windows](https://img.shields.io/badge/Windows-.exe_included-0078D6?logo=windows&logoColor=white)

</div>

---

## ✨ How it works

Run the script, answer two prompts and get your codes:

```text
Enter title for QRCode : my-site
what does the QRCode have to say? : https://github.com/Arashomranpour
```

The script creates the QR code with **pyqrcode**, writes `my-site.png` and `my-site.svg`, and moves both into a `QRs/` folder.

A ready-to-run Windows build (`dist/qr.exe`, packaged with PyInstaller) is included, so no Python installation is needed on Windows.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/QR-generator.git
cd QR-generator
pip install pyqrcode pypng
python qr.py
```

Rebuild the executable:

```bash
pip install pyinstaller
pyinstaller --onefile qr.py
```

## 📁 Project Structure

```
.
├── qr.py         # QR generator script
├── qr.spec       # PyInstaller spec
└── dist/qr.exe   # Windows executable
```

## 🛠️ Tech Stack

`Python` · `pyqrcode` · `PyInstaller`
