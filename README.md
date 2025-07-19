# Birthday Telegram Bot 🎉

A simple GitHub Actions bot that checks your Google Calendar daily, generates a custom birthday wish with OpenAI, and sends it to you on Telegram.

## How to use

1. **Create Google Calendar API credentials (service account)** → Save JSON → base64 encode it → store as `GOOGLE_CREDS_B64` secret.

2. **Create OpenAI API key** → store as `OPENAI_API_KEY`.

3. **Create a Telegram Bot with BotFather** → store `TELEGRAM_BOT_TOKEN`.

4. **Get your Telegram chat ID** → store `TELEGRAM_CHAT_ID`.

5. Push this repo to GitHub → add the above secrets in **Settings → Secrets → Actions**.

6. The bot runs daily (or manually) → checks for birthdays → sends you a birthday wish.

Enjoy! 🎂
