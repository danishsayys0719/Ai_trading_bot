import json
import telebot

# Load config.json
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

BOT_TOKEN = config.get("BOT_TOKEN")   # FIXED
CHAT_ID = config.get("CHAT_ID")       # FIXED

if BOT_TOKEN is None or CHAT_ID is None:
    raise SystemExit("Missing BOT_TOKEN or CHAT_ID in config.json")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Bot is running!")

def send_signal(text):
    bot.send_message(CHAT_ID, text)

if __name__ == "__main__":
    print("Starting bot with CHAT_ID =", CHAT_ID)
    bot.polling()
