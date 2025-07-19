import base64
import os
from datetime import datetime, timedelta
from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
import openai
import config

# ---- Decode Google creds ----
with open(config.GOOGLE_CREDS_PATH, "wb") as f:
    f.write(base64.b64decode(config.GOOGLE_CREDS_B64))

# ---- Setup Google Calendar ----
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

creds = service_account.Credentials.from_service_account_file(
    config.GOOGLE_CREDS_PATH, scopes=SCOPES)
service = build('calendar', 'v3', credentials=creds)

# ---- Get today's date range ----
now = datetime.utcnow().isoformat() + 'Z'
end_of_day = (datetime.utcnow() + timedelta(days=1)).isoformat() + 'Z'

# ---- Get events ----
events_result = service.events().list(
    calendarId=config.CALENDAR_ID,
    timeMin=now,
    timeMax=end_of_day,
    singleEvents=True,
    orderBy='startTime'
).execute()

events = events_result.get('items', [])

birthdays = []
for event in events:
    summary = event.get('summary', '').lower()
    if "birthday" in summary:
        birthdays.append(event['summary'])

if not birthdays:
    print("No birthdays today.")
else:
    print(f"Found birthdays: {birthdays}")

    openai.api_key = config.OPENAI_API_KEY

    for bday in birthdays:
        person = bday.replace("Birthday:", "").strip()
        prompt = f"Write a warm, short birthday message for {person}."

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a warm assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        wish = response['choices'][0]['message']['content']
        print(f"Generated: {wish}")

        url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": wish
        }
        r = requests.post(url, json=payload)

        if r.status_code == 200:
            print("Sent to Telegram ✅")
        else:
            print(f"Failed to send: {r.text}")
