import json
import telebot

# Load config.json
with open("config.json") as f:
    config = json.load(f)

BOT_TOKEN = config["8226369849:AAFcWM34yciiTCTAy-3q-F0sD6E5dsSBpsc"]
CHAT_ID = config["8183172862"]

bot = telebot.TeleBot(8226369849:AAFcWM34yciiTCTAy-3q-F0sD6E5dsSBpsc)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.8183172862, "Bot is running!")

def send_signal(text):
    bot.send_message(8183172862, text)

bot.pollingf()
