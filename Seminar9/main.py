## Пример преподавателя на pyTelegramBotAPI. 

# import telebot
# from telebot import types
# from telegram import ReplyKeyboardMarkup, KeyboardButton

# token = "5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg"
# bot = telebot.TeleBot("5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg")

# @bot.message_handler(commands=["start"])
# def start (m, res=False):
#         bot.send_message(m.chat.id, "Я на связи. Напиши мне что-нибудь.")

# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     s = message.text
#     c = "абв"
#     bot.send_message(message.chat.id, message.text)

# bot.polling(none_stop = True, interval = 0)

## Пример коллеги на python-telegram-bot. 
# Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# app.add_handler(CommandHandler("edit", edit_txt))
# async def edit_txt (update: Update, ContextType.DEFAULT_TYPE):
#     user_mes = update.message.text
#     user_mes = user_mes[5:]
#     c = "абв"
#     user_mes = list(filter(lambda user_mes: not c in user_mes, user_mes.split()))
#     user_mes = ' ',join(user_mes)
#     await update.message.reply_text(user_mes)

## Пример-Конфетки от Анатолия Щербакова на pyTelegramBotAPI. 

import telebot
from random import randint as ran

token = '5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg'
bot = telebot.TeleBot(token)

candies = 0
max_candies = 28

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')

@bot.message_handler(commands=["game"])
def handle_text(message):
    global candies
    candies = 101
    bot.send_message(message.chat.id, f'На столе лежит {candies} конфет')
# game(candies, max_candies)

@bot.message_handler(content_types=["text"])
def inputs(message):
    global candies
    if candies <= 0:
        bot.send_message(message.chat.id, f'Игра окончена')
        handle_text(message)
        return
    else: bot.send_message(message.chat.id, f'Возьмите конфеты:')
    try:
        can = int(message.text)
        candies = candies - can
        bot.send_message(message.chat.id, f'Конфет осталось {candies}')
        ran_can = ran(1, max_candies)
        candies = candies - ran_can
        bot.send_message(message.chat.id, f'Бот взял {ran_can} конфет, их осталось {candies}')
    except ValueError:
        bot.send_message(message.chat.id, f'Ошибка. Введите число...')

bot.polling(none_stop=True, interval=0)