import os

GOOGLE_CREDS_B64 = os.getenv("GOOGLE_CREDS_B64")  # base64 of credentials.json
GOOGLE_CREDS_PATH = "credentials.json"
CALENDAR_ID = "primary"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
