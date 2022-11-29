# import print1
import telebot
from telebot import types
# import delete
# import edit
# import add
# import search
from telegram import ReplyKeyboardMarkup, KeyboardButton

token = "5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg"
bot = telebot.TeleBot("5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg")

@bot.message_handler(commands=["start"])
def start (m, res=False):
        bot.send_message(m.chat.id, "Я на связи. Напиши мне что-нибудь.")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    s = message.text
    c = "абв"
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True, interval = 0)