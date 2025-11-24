import json
import ccxt
from telegram import Bot
from telegram.ext import CommandHandler, Updater

# Load config
with open("config.json") as f:
    config = json.load(f)

telegram_token = config["telegram_token"]

# Telegram bot setup
bot = Bot(token=telegram_token)
updater = Updater(token=telegram_token, use_context=True)
dispatcher = updater.dispatcher

# Simple /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="AI Trading Bot is online!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start bot
updater.start_polling()
print("Bot is running...")
updater.idle()