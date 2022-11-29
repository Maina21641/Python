import search
import add
import delete
import telebot
from telebot import types
from telegram import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg", parse_mode=None)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if message.text == "/Start":
        bot.send_message(message.from_user.id, "Привет, напиши или нажми на /Help, чтобы вызвать меню.")
    
    elif message.text == "/Help":
        bot.send_message(message.from_user.id, "Вот, что я могу:\nВыбери /1_Print_all_base, чтобы отобразить весь список контактов.\nВыбери /2_Search_entry, чтобы найти совпадение по элементу.\nВыбери /3_Add_entry, чтобы добавить новый контакт.\nВыбери /4_Delete_entry, чтобы удалить контакт.\nВыберите /5_Out, чтобы выйти из меню.")
    
    elif message.text == "/1_Print_all_base":
        with open('HomeWork8\\employees.csv', encoding="utf-8") as data:
            for line in data:
                bot.send_message(message.from_user.id, f"{line.replace(',', ' ')}")
            bot.send_message(message.from_user.id, "Что делать дальше?\nВыбери /1_Print_all_base, чтобы отобразить весь список контактов.\nВыбери /2_Search_entry, чтобы найти совпадение по элементу.\nВыбери /3_Add_entry, чтобы добавить новый контакт.\nВыбери /4_Delete_entry, чтобы удалить контакт.\nВыберите /5_Out, чтобы выйти из меню.")

    elif message.text == "/2_Search_entry":
        bot.send_message(message.from_user.id, f"Введите, что нужно найти в списке контактов?")
        bot.register_next_step_handler(message, sear)

    elif message.text == "/3_Add_entry":
        bot.send_message(message.from_user.id, f'Введите ID - номер записи: ')
        bot.register_next_step_handler(message, num)

    elif message.text == "/4_Delete_entry":
        bot.send_message(message.from_user.id, f'Введите ID - номер записи для удаления.')
        bot.register_next_step_handler(message, Del)

    elif message.text == "/5_Out":
        bot.send_message(message.from_user.id, f'Спасибо за визит, сообщи, если я буду полезен!')

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши или нажми на /Help.")

@bot.message_handler(content_types=["text"])
def sear(message):
    s = message.text
    with open('HomeWork8\\employees.csv', 'r', encoding="utf-8") as data:
        for line in data:
            if s in line:
                bot.send_message(message.from_user.id, f"Найдено:\n{line}")
        bot.send_message(message.from_user.id, "Если совпадений нет, попробуйте указать другой элемент. Помните про регистр и клавишу CAPS.\nВернуться в /2_Search_entry?\nВернуться в /Help?")

contacts = [None]*6
def num(message):
    contacts[0] = message.text
    bot.send_message(message.from_user.id, "Введите фамилию: ")
    bot.register_next_step_handler(message, surname)
def surname(message):
    contacts[1] = message.text
    bot.send_message(message.from_user.id, "Введите имя: ")
    bot.register_next_step_handler(message, name)
def name(message):
    contacts[2] = message.text
    bot.send_message(message.from_user.id, "Введите телефон: ")
    bot.register_next_step_handler(message, number)
def number(message):
    contacts[3] = message.text
    bot.send_message(message.from_user.id, "Введите название компании: ")
    bot.register_next_step_handler(message, comment1)
def comment1(message):
    contacts[4] = message.text
    bot.send_message(message.from_user.id, "Введите должность: ")
    bot.register_next_step_handler(message, comment2)
def comment2(message):
    contacts[5] = message.text
    print(contacts)
    add.newstring(contacts)
    bot.send_message(message.from_user.id, f"Добавлены следующие даннные:\n{contacts}\nНажми на /1_Print_all_base, чтобы отобразить весь список контактов.\nВернуться в /Help?")

def Del(message):
    s=message.text
    lines = []
    with open('HomeWork8\\employees.csv', 'r', encoding="utf-8") as data:
            for line in data:
                if not s in line: lines += line
    with open('HomeWork8\\employees.csv', 'w', encoding="utf-8") as data:
            data.writelines(lines)
    bot.send_message(message.from_user.id, 'Удаление произведено. Что делать дальше?\nВыбери /1_Print_all_base, чтобы отобразить весь список контактов.\nВыбери /2_Search_entry, чтобы найти совпадение по элементу.\nВыбери /3_Add_entry, чтобы добавить новый контакт.\nВыбери /4_Delete_entry, чтобы удалить контакт.\nВыберите /5_Out, чтобы выйти из меню.')

print("Server start")
bot.polling(none_stop=True, interval=0)