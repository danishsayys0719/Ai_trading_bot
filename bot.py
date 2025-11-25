import telebot

BOT_TOKEN = "8226369849:AAFcWM34yciiTCTAy-3q-F0sD6E5dsSBpsc"
CHAT_ID = "https://t.me/Sniper0719_bot"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Bot is running!")

def send_signal(text):
    bot.send_message(CHAT_ID, text)

bot.polling()
