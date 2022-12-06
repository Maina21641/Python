
import datetime
import telebot

bot = telebot.TeleBot("5734750462:AAGVLmbk-P3_UgEH4cu0M14AX0EYAdu-4wg")

def my_log(message):
    my_string = f"{datetime.datetime.now()}--{message.from_user.id}--{message.text}\n"
    with open("HomeWork10\\logger.txt", "a") as file:
        file.write(my_string)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if message.text == "/Start":
        bot.send_message(message.from_user.id, "Я простой калькулятор, у меня мало функций. Недавно в список добавилась возможность операций с комплексными числами. Напиши или нажми на /Help, чтобы вызвать меню и посмотреть, что я могу.")
        my_log(message)

    elif message.text == "/Help":
        bot.send_message(message.from_user.id, "Вот, что я могу:\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Complex, чтобы провести операции с комплексными числами.\nВыбери /6_Export_Logs, чтобы скачать файл .txt и посмотреть логи.\nВыберите /7_Out, чтобы выйти из меню.")
        my_log(message)

    elif message.text == "/1_Sum":
        bot.send_message(message.from_user.id, f"Введите первое число.")
        bot.register_next_step_handler(message, sum1)
        my_log(message)

    elif message.text == "/2_Sub":
        bot.send_message(message.from_user.id, f"Введите первое число.")
        bot.register_next_step_handler(message, sub1)
        my_log(message)

    elif message.text == "/3_Mult":
        bot.send_message(message.from_user.id, f'Введите первое число.')
        bot.register_next_step_handler(message, mult1)
        my_log(message)

    elif message.text == "/4_Div":
        bot.send_message(message.from_user.id, f'Введите первое число.')
        bot.register_next_step_handler(message, div1)
        my_log(message)

    elif message.text == "/5_Complex":
        act = bot.send_message(message.chat.id,
                           'Введите выражение с комплексными числами в формате \n(a+bj)+(c+dj),\n где вместо знака '
                           'сложения может быть любое из доступных действий (+, -, *, /): ')  # вводим выражение
        bot.register_next_step_handler(act, action_with_complex_numbers)
        my_log(message)

    elif message.text == "/6_Export_Logs":
        bot.send_document(chat_id=message.from_user.id, document=open("HomeWork10\\logger.txt", "rb"))
        bot.send_message(message.from_user.id, "Что-нибудь еще?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Complex, чтобы провести операции с комплексными числами.\nВыбери /6_Export_Logs, чтобы скачать файл .txt и посмотреть логи.\nВыберите /7_Out, чтобы выйти из меню.")
        my_log(message)
        
    elif message.text == "/7_Out":
        bot.send_message(message.from_user.id, f'Спасибо за визит, сообщи, если я буду полезен!')
        my_log(message)

    else:
        bot.send_message(message.from_user.id, "Привет, я тебя не понимаю. Напиши или нажми на /Start.")
        my_log(message)

def sum1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, sum2)
    my_log(message)

def sum2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} + {b} = {a + b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Complex, чтобы провести операции с комплексными числами.\nВыбери /6_Export_Logs, чтобы скачать файл .txt и посмотреть логи.\nВыберите /7_Out, чтобы выйти из меню.")
    my_log(message)

def sub1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, sub2)
    my_log(message)

def sub2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} - {b} = {a - b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Complex, чтобы провести операции с комплексными числами.\nВыбери /6_Export_Logs, чтобы скачать файл .txt и посмотреть логи.\nВыберите /7_Out, чтобы выйти из меню.")
    my_log(message)

def mult1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, mult2)
    my_log(message)

def mult2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} * {b} = {a * b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Complex, чтобы провести операции с комплексными числами.\nВыбери /6_Export_Logs, чтобы скачать файл .txt и посмотреть логи.\nВыберите /7_Out, чтобы выйти из меню.")
    my_log(message)

def div1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, div2)
    my_log(message)

def div2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} / {b} = {a / b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Complex, чтобы провести операции с комплексными числами.\nВыбери /6_Export_Logs, чтобы скачать файл .txt и посмотреть логи.\nВыберите /7_Out, чтобы выйти из меню.")
    my_log(message)

def action_with_complex_numbers(message):
    bot.send_message(message.chat.id,'Ответ:')
    bot.send_message(message.chat.id, eval(message.text))
    bot.send_message(message.from_user.id, "Что-нибудь еще?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Complex, чтобы провести операции с комплексными числами.\nВыбери /6_Export_Logs, чтобы скачать файл .txt и посмотреть логи.\nВыберите /7_Out, чтобы выйти из меню.")
    my_log(message)

print("Server start")
bot.polling(none_stop=True, interval=0)