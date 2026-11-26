
from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_message(chat_id, text):
    requests.post(TELEGRAM_API, data={
        "chat_id": chat_id,
        "text": text
    }, timeout=15)

@app.route("/", methods=["GET"])
def home():
    return "Gold Forex Signals Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    message = data.get("message", {})
    chat = message.get("chat", {})
    chat_id = chat.get("id")
    text = message.get("text", "")

    if not chat_id:
        return "OK"

    if text == "/start":
        reply = "🤖 به Gold Forex Signals خوش آمدید!\n\n/analysis - تحلیل بازار\n/signals - وضعیت سیگنال‌ها\n/help - راهنما\n/about - درباره ربات"

    elif text == "/help":
        reply = "دستورات ربات:\n/start\n/analysis\n/signals\n/about"

    elif text == "/analysis":
        reply = "📊 تحلیل تکنیکال طلا\nبرای تحلیل دقیق، نماد و تایم‌فریم را بررسی کنید. این پیام توصیه مالی نیست."

    elif text == "/signals":
        reply = "📡 در حال حاضر سیگنال تأییدشده‌ای ثبت نشده است."

    elif text == "/about":
        reply = "Gold Forex Signals\nربات اطلاع‌رسانی و تحلیل بازار طلا و فارکس."

    else:
        reply = "دستور نامعتبر است. برای راهنما /help را بفرستید."

    send_message(chat_id, reply)
    return "OK"

if __name__ == "__main__":
    app.run()
