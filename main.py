import os
import datetime
import asyncio
from dotenv import load_dotenv
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from telegram import Update

# IMPORT SERVICES
from src.services.reminder_service import add_reminder, start_reminder_thread
from src.services.symptom_checker_service import SymptomCheckerService
from src.services.food_scanner_service import FoodScannerService
from src.api_clients.llm_client import GeminiClient
from src.data.symptoms import symptoms_to_diseases
from src.database.init_db import init_db
from src.utils.logger import logger
from src.exception.exception_handler import catch_async_exceptions, run_safe

#  LOAD CONFIG 
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not TELEGRAM_TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN not set in .env")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not set in .env")


# INIT SERVICES 
symptom_service = SymptomCheckerService(symptoms_to_diseases, GEMINI_API_KEY)
llm_client = GeminiClient(GEMINI_API_KEY)


# TOOL FUNCTIONS 
def tool_symptom_check(symptoms_str: str) -> str:
    symptoms = [s for s in (symptoms_str or "").split() if s]
    result = symptom_service.check(symptoms)
    return (
        f"🤒 Symptoms: {', '.join(symptoms) if symptoms else '—'}\n"
        f"🧾 Possible diseases: {', '.join(result['predicted_diseases'])}\n"
        f"💡 Advice: {result['llm_response']}"
    )


def tool_food_scan(_: str) -> str:
    return "📸 Please send an image after /foodscan."


def tool_add_reminder(chat_id: int, message: str, remind_at: datetime.datetime) -> str:
    return add_reminder(chat_id=chat_id, message=message, remind_at=remind_at)


# COMMAND HANDLERS 
@catch_async_exceptions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I can chat with you, check symptoms, scan food, and set reminders!\n\n"
        "🔹 Try commands:\n"
        "/symptom cough fever\n"
        "/foodscan (send with a photo)\n"
        "💬 Or just talk naturally, and I’ll figure it out!"
    )


#  MESSAGE HANDLER 
@catch_async_exceptions
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id
    text = update.message.text or ""

    logger.info(f"User({user_id}) said: {text}")

    response = llm_client.run_agent(
        query=text,
        tools={
            "symptom_check": tool_symptom_check,
            "food_scan": tool_food_scan,
            "add_reminder": tool_add_reminder,
            "_chat_id": user_id,
        },
    )

    await update.message.reply_text(response)


#  IMAGE HANDLER 
@catch_async_exceptions
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    image_path = "src/test/received_image.jpg"
    await photo_file.download_to_drive(image_path)

    result = FoodScannerService.scan(image_path)
    response = llm_client.ask(
        f"Food scan raw result:\n{result}\nSummarize politely for user."
    )
    await update.message.reply_text(response)


#   MAIN ENTRY  
def main():
    init_db()

    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Register handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    async def on_startup(app):
        loop = asyncio.get_running_loop()
        start_reminder_thread(app.bot, loop)

    app.post_init = on_startup

    logger.info("🤖 Bot started (conversation + tools mode)...")
    app.run_polling()


if __name__ == "__main__":
    run_safe(main)
