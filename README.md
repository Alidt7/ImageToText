# Telegram OCR Bot 

A simple Telegram bot that extracts text from images using [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

---

## 📦 Features

* Accepts images sent via Telegram.
* Enhances and processes the image.
* Extracts readable text using Tesseract.
* Sends back the extracted text.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Alidt7/ImageToText.git
cd telegram-ocr-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Also make sure Tesseract OCR is installed and available in your PATH.

* Windows: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
* Linux (Ubuntu):

  ```bash
  sudo apt update && sudo apt install tesseract-ocr
  ```

### 3. Configure `config.py`

Create a `config.py` file in the project root with the following content:

```python
from typing import final

TOKEN: final = 'your_bot_token_here'
BOT_USERNAME: final = '@your_bot_username'
ADMIN_ID: final = 123456789
ADMIN_USERNAME: final = '@your_admin_username'
```

Do **not** share this file publicly. You can add it to `.gitignore` to keep it private.

### 4. Run the Bot

```bash
python main.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🧠 Author

Created by **Ali Dianati** — feel free to contribute or suggest improvements!

---

## ✨ Example

Just send a photo of a document or text via Telegram to the bot, and it will reply with the extracted text automatically.

Happy automating! 🚀
