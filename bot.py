cat > bot.py <<'PY'
import json
import telebot

# Load config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

BOT_TOKEN = config.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = config.get("CHAT_ID")

if BOT_TOKEN is None or CHAT_ID is None:
    raise SystemExit("Missing TELEGRAM_BOT_TOKEN or CHAT_ID in config.json")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Bot is running!")

def send_signal(text):
    # CHAT_ID may be string; telebot accepts both string and int
    bot.send_message(CHAT_ID, text)

if __name__ == "__main__":
    # Simple sanity test before polling
    print("Starting bot with CHAT_ID =", CHAT_ID)
    bot.polling()
PY
