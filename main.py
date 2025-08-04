from config import TOKEN, BOT_USERNAME, ADMIN_ID, ADMIN_USERNAME
import logging
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import telebot
import time

#-------- Logging config --------

logging.basicConfig(
  level=logging.INFO,
  encoding='utf-8',
  format="[%(levelname)s] (%(asctime)s): %(message)s (line: %(lineno)s)",
  datefmt='%Y/%m/%d %I:%M:%S %p'
)

#----------- Start handler -----------
logging.info("Connecting to the bot...")
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
  logging.info("User started the bot.")
  bot.send_message(message.chat.id, f"Hello {message.from_user.first_name}, I am {BOT_USERNAME}.\nSend a photo to extract text from it.")

#----------- Text extraction handler -----------

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
  logging.info("User sent photo...")
  bot.send_message(message.chat.id, "Processing your photo...🌐")
  try:
    # Step 1: Download the photo
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open('temp_image.jpg', 'wb') as new_file:
      new_file.write(downloaded_file)

    # Step 2: Open and enhance the image
    image = Image.open('temp_image.jpg')
        
    # Convert to grayscale for better OCR
    image = image.convert('L')
        
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)

    # Step 3: OCR extraction with config
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)

    logging.info("Text extracted from the image.")

    if text.strip():
      bot.send_message(message.chat.id, "Text extracted successfully! ✅")
      bot.send_message(message.chat.id, "Extracted Text:")
      time.sleep(1)
      bot.send_message(message.chat.id, text)
    else:
      bot.send_message(message.chat.id, "No text found in the image.")

  except Exception as e:
    logging.error(f"Error processing photo: {e}")
    bot.send_message(message.chat.id, "An error occurred while processing the image.")
  logging.info("Polling...")


logging.info("Polling...")
bot.polling(none_stop=True)
