import json
import ccxt
from telegram import Bot
from telegram.ext import CommandHandler, Updater

# Load config
with open("config.json") as f:
    config = json.load(f)

8525361188:AAFE1LBMuibVdoDs5AWoTQFeSswKDmBlAKo = config["8525361188:AAFE1LBMuibVdoDs5AWoTQFeSswKDmBlAKo"]

# Telegram bot setup
bot = Bot(token=8525361188:AAFE1LBMuibVdoDs5AWoTQFeSswKDmBlAKo)
updater = Updater(token=8525361188:AAFE1LBMuibVdoDs5AWoTQFeSswKDmBlAKo, use_context=True)
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