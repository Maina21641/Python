import io
from telebot import types
import telebot
import HtmlFormat as html

bot = telebot.TeleBot("5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if message.text == "/Start":
        bot.send_message(message.from_user.id, "Я телефонный справочник."
        "\nНапиши или нажми на /Help, чтобы вызвать меню и посмотреть способы взаимодействия со мной.")
    
    elif message.text == "/Help":
        bot.send_message(message.from_user.id, "Вот, что я могу:"
        "\n/1_Show_PhoneBook. Выбери, чтобы посмотреть все контакты телефонного справочника."
        "\n/2_Search. Выбери, чтобы найти все совпадения."
        "\n/3_Add. Выбери, чтобы добавить новый контакт."
        "\n/4_Delete. Выбери, чтобы удалить контакт."
        "\n/5_Download_To_TXT. Выбери, чтобы скачать файл телефонного справочника формата txt."
        "\n/6_Download_To_CSV. Выбери, чтобы скачать файл телефонного справочника формата csv."
        "\n/7_Download_To_HTML. Выбери, чтобы скачать файл телефонного справочника формата html."
        "\n/8_Upload. Выбери, чтобы загрузить файл на сервер."
        "\n/9_Out. Выбери, чтобы выйти из меню.")
    
    elif message.text == "/1_Show_PhoneBook":
        with open('HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.txt', encoding="utf-8") as data:
            for line in data:
                bot.send_message(message.from_user.id, f"{line.replace(',', ' ')}")
            bot.send_message(message.from_user.id, "Что делать дальше?"
            "\n/1_Show_PhoneBook. Выбери, чтобы посмотреть все контакты телефонного справочника."
            "\n/2_Search. Выбери, чтобы найти все совпадения."
            "\n/3_Add. Выбери, чтобы добавить новый контакт."
            "\n/4_Delete. Выбери, чтобы удалить контакт."
            "\n/5_Download_To_TXT. Выбери, чтобы скачать файл телефонного справочника формата txt."
            "\n/6_Download_To_CSV. Выбери, чтобы скачать файл телефонного справочника формата csv."
            "\n/7_Download_To_HTML. Выбери, чтобы скачать файл телефонного справочника формата html."
            "\n/8_Upload. Выбери, чтобы загрузить файл на сервер."
            "\n/9_Out. Выбери, чтобы выйти из меню.")

    elif message.text == "/2_Search":
        bot.send_message(message.from_user.id, f"Введите, что нужно найти в списке контактов?")
        bot.register_next_step_handler(message, sear)

    elif message.text == "/3_Add":
        bot.send_message(message.from_user.id, f'Введите ФИО: ')
        bot.register_next_step_handler(message, names)

    elif message.text == "/4_Delete":
        bot.send_message(message.from_user.id, f'Введите ФИО или номер телефона для удаления контакта.')
        bot.register_next_step_handler(message, delete)

    elif message.text == "/5_Download_To_TXT":
        bot.send_message(message.from_user.id, f"Чтобы скачать, нажми на файл.")
        bot.send_document(message.from_user.id, document=open('HomeWork9//3PhoneBookBotTelegramm//Phonebook.txt', 'rb'))
        bot.send_message(message.from_user.id, "Что еще пожелаешь?"
        "\n/1_Show_PhoneBook. Выбери, чтобы посмотреть все контакты телефонного справочника."
        "\n/2_Search. Выбери, чтобы найти все совпадения."
        "\n/3_Add. Выбери, чтобы добавить новый контакт."
        "\n/4_Delete. Выбери, чтобы удалить контакт."
        "\n/5_Download_To_TXT. Выбери, чтобы скачать файл телефонного справочника формата txt."
        "\n/6_Download_To_CSV. Выбери, чтобы скачать файл телефонного справочника формата csv."
        "\n/7_Download_To_HTML. Выбери, чтобы скачать файл телефонного справочника формата html."
        "\n/8_Upload. Выбери, чтобы загрузить файл на сервер."
        "\n/9_Out. Выбери, чтобы выйти из меню.")
    
    elif message.text == "/6_Download_To_CSV":
        bot.send_message(message.from_user.id, f"Чтобы скачать, нажми на файл.")
        bot.send_document(message.from_user.id, document=open('HomeWork9//3PhoneBookBotTelegramm//Phonebook.csv', 'rb'))
        bot.send_message(message.from_user.id, "Что еще пожелаешь?"
        "\n/1_Show_PhoneBook. Выбери, чтобы посмотреть все контакты телефонного справочника."
        "\n/2_Search. Выбери, чтобы найти все совпадения."
        "\n/3_Add. Выбери, чтобы добавить новый контакт."
        "\n/4_Delete. Выбери, чтобы удалить контакт."
        "\n/5_Download_To_TXT. Выбери, чтобы скачать файл телефонного справочника формата txt."
        "\n/6_Download_To_CSV. Выбери, чтобы скачать файл телефонного справочника формата csv."
        "\n/7_Download_To_HTML. Выбери, чтобы скачать файл телефонного справочника формата html."
        "\n/8_Upload. Выбери, чтобы загрузить файл на сервер."
        "\n/9_Out. Выбери, чтобы выйти из меню.")

    elif message.text == "/7_Download_To_HTML":
        bot.send_message(message.from_user.id, f"Чтобы скачать, нажми на файл.")
        bot.send_document(message.from_user.id, document=open('HomeWork9//3PhoneBookBotTelegramm//Phonebook.html', 'rb'))
        bot.send_message(message.from_user.id, "Что еще пожелаешь?"
        "\n/1_Show_PhoneBook. Выбери, чтобы посмотреть все контакты телефонного справочника."
        "\n/2_Search. Выбери, чтобы найти все совпадения."
        "\n/3_Add. Выбери, чтобы добавить новый контакт."
        "\n/4_Delete. Выбери, чтобы удалить контакт."
        "\n/5_Download_To_TXT. Выбери, чтобы скачать файл телефонного справочника формата txt."
        "\n/6_Download_To_CSV. Выбери, чтобы скачать файл телефонного справочника формата csv."
        "\n/7_Download_To_HTML. Выбери, чтобы скачать файл телефонного справочника формата html."
        "\n/8_Upload. Выбери, чтобы загрузить файл на сервер."
        "\n/9_Out. Выбери, чтобы выйти из меню.")

    elif message.text == "/8_Upload":
        bot.send_message(message.from_user.id, f"Загрузи свой файл в телеграмм.")
        
    elif message.text == "/9_Out":
            bot.send_message(message.from_user.id, f'Спасибо за визит, сообщи, если я буду полезен!')
    else:
        bot.send_message(message.from_user.id, "Привет, я тебя не понимаю. Напиши или нажми на /Start.")

# Функция вызывается, как только в сообщение попадает файл. 
# Другими словами, следовать меню для этого не нужно.

@bot.message_handler(content_types=['document'])
def handle_docs(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'HomeWork9//3PhoneBookBotTelegramm//' + message.document.file_name
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Спасибо, я сохраню это."
        "\nЯ обновлю информацию, как только проверю ее."
        "\nЧто-нибудь еще?"
        "\n/1_Show_PhoneBook. Выбери, чтобы посмотреть все контакты телефонного справочника."
        "\n/2_Search. Выбери, чтобы найти все совпадения."
        "\n/3_Add. Выбери, чтобы добавить новый контакт."
        "\n/4_Delete. Выбери, чтобы удалить контакт."
        "\n/5_Download_To_TXT. Выбери, чтобы скачать файл телефонного справочника формата txt."
        "\n/6_Download_To_CSV. Выбери, чтобы скачать файл телефонного справочника формата csv."
        "\n/7_Download_To_HTML. Выбери, чтобы скачать файл телефонного справочника формата html."
        "\n/8_Upload. Выбери, чтобы загрузить файл на сервер."
        "\n/9_Out. Выбери, чтобы выйти из меню.")
    except Exception as e:
        bot.reply_to(message, e)

@bot.message_handler(content_types=["text"])
def sear(message):
    s = message.text
    with open('HomeWork9//3PhoneBookBotTelegramm//Phonebook.txt', 'r', encoding="utf-8") as data:
        for line in data:
            if s in line:
                bot.send_message(message.from_user.id, f"Найдено:\n{line}")
        bot.send_message(message.from_user.id, "Если совпадений нет, попробуйте указать другой элемент."
        "\nПомните про регистр и клавишу CAPS."
        "\nВернуться в /2_Search?"
        "\nВернуться в /Help?")

contacts = [None]*2
def names(message):
    contacts[0] = message.text
    bot.send_message(message.from_user.id, "Введите телефон: ")
    bot.register_next_step_handler(message, phone)
def phone(message):
    contacts[1] = message.text
    print(contacts)
    newstring(contacts)
    bot.send_message(message.from_user.id, f"В файл Phonebook.txt добавлены следующие даннные:\n{contacts}"
    "\nНажми на /1_Show_PhoneBook, чтобы отобразить весь список контактов."
    "\nИли нажми /Help, чтобы вернуться в меню.")
def newstring(contacts):
    bazaopen = open("HomeWork9//3PhoneBookBotTelegramm//Phonebook.txt", "a", encoding = 'utf-8')
    bazaopen.write(f"\n{contacts[0]}:")
    bazaopen.write(f" {contacts[1]}")
    bazaopen.close()
    bazaopen1 = open("HomeWork9//3PhoneBookBotTelegramm//Phonebook.csv", "a", encoding = 'utf-8')
    bazaopen1.write(f"\n{contacts[0]}:")
    bazaopen1.write(f" {contacts[1]}")
    bazaopen1.close()
    html.GoToHtml()

def delete(message):
    s=message.text
    lines = []
    with open('HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.txt', 'r', encoding="utf-8") as data:
        with open('HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.csv', 'r', encoding="utf-8") as data:
            for line in data:
                if not s in line: lines += line
    with open('HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.txt', 'w', encoding="utf-8") as data:
        data.writelines(lines)
    with open('HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.csv', 'w', encoding="utf-8") as data:
        data.writelines(lines)
    # import fileinput
    # for line in fileinput.FileInput("HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.txt",inplace=1):
    #     if line.rstrip():
    #         print(line)
    # for line in fileinput.FileInput("HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.csv",inplace=1):
    #     if line.rstrip():
    #         print(line)
    html.GoToHtml()
    bot.send_message(message.from_user.id, "Удаление произведено."
    "\nЧто делать дальше?"
    "\n/1_Show_PhoneBook. Выбери, чтобы посмотреть все контакты телефонного справочника."
    "\n/2_Search. Выбери, чтобы найти все совпадения."
    "\n/3_Add. Выбери, чтобы добавить новый контакт."
    "\n/4_Delete. Выбери, чтобы удалить контакт."
    "\n/5_Download_To_TXT. Выбери, чтобы скачать файл телефонного справочника формата txt."
    "\n/6_Download_To_CSV. Выбери, чтобы скачать файл телефонного справочника формата csv."
    "\n/7_Download_To_HTML. Выбери, чтобы скачать файл телефонного справочника формата html."
    "\n/8_Upload. Выбери, чтобы загрузить файл на сервер."
    "\n/9_Out. Выбери, чтобы выйти из меню.")

print("Server start")
bot.polling(none_stop=True, interval=0)