cat > bot.py <<'PY'
import json
import sys

# Minimal debug loader
try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except Exception as e:
    print("ERROR reading config.json:", repr(e))
    sys.exit(1)

BOT_TOKEN = config.get("BOT_TOKEN")
CHAT_ID = config.get("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    print("CONFIG KEYS MISSING. Found keys:", list(config.keys()))
    sys.exit(1)

print("Config loaded OK. BOT_TOKEN length:", len(BOT_TOKEN))
print("CHAT_ID value:", CHAT_ID)

# Do not import telebot until we confirm basic config is OK
try:
    import telebot
except Exception as e:
    print("telebot import failed (is it installed?):", repr(e))
    sys.exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Bot is running!")

if __name__ == "__main__":
    print("Starting bot.polling()")
    bot.polling()
PY
