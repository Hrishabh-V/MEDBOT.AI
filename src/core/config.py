# src/config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Database
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "medbot")

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")

# USDA API

USDA_API_KEY = os.getenv("USDA_API_KEY", "")
USDA_API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
#GEmini api 
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

# Model
MODEL_PATH = os.getenv("MODEL_PATH", "keras_Model1.h5")
LABELS_PATH = os.getenv("LABELS_PATH", "labels.txt")
