from telebot import TeleBot
from src.services.food_scanner_service import FoodScannerService
from src.utils.logger import logger
import os

def register_food_handler(bot: TeleBot):
    @bot.message_handler(content_types=['photo'])
    def handle_food_image(message):
        try:
            logger.debug(f"Received photo from chat_id={message.chat.id}")

            # Validate photo
            if not message.photo:
                bot.send_message(message.chat.id, "⚠️ No photo found in the message.")
                return

            try:
                file_info = bot.get_file(message.photo[-1].file_id)
            except Exception as e:
                logger.exception("Failed to retrieve file info")
                bot.send_message(message.chat.id, f"⚠️ Could not retrieve photo info: {str(e)}")
                return

            try:
                downloaded_file = bot.download_file(file_info.file_path)
            except Exception as e:
                logger.exception("Failed to download file from Telegram servers")
                bot.send_message(message.chat.id, f"⚠️ Could not download the image: {str(e)}")
                return

            # Save file locally
            try:
                image_path = f"/tmp/{os.path.basename(file_info.file_path)}"
                with open(image_path, "wb") as f:
                    f.write(downloaded_file)
                logger.debug(f"Image saved to {image_path}")
            except Exception as e:
                logger.exception("Failed to save image locally")
                bot.send_message(message.chat.id, f"⚠️ Could not save the image: {str(e)}")
                return

            # Process image with FoodScannerService
            try:
                result = FoodScannerService.san(image_path)
                bot.send_message(message.chat.id, result)
            except Exception as e:
                logger.exception("Error while scanning food")
                bot.send_message(message.chat.id, f"⚠️ Error scanning food: {str(e)}")

        except Exception as e:
            logger.exception("Unexpected error in handle_food_image")
            bot.send_message(message.chat.id, f"⚠️ Unexpected error: {str(e)}")
