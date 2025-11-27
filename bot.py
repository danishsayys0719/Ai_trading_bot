import json
import telebot

with open("config.json") as f:
    config = json.load(f)

BOT_TOKEN = config["BOT_TOKEN"]
CHAT_ID = config["CHAT_ID"]

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Bot is running!")

def send_signal(text):
    bot.send_message(CHAT_ID, text)

bot.polling()
