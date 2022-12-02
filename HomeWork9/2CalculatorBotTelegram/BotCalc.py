
import telebot

bot = telebot.TeleBot("ТутТвойТокен")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if message.text == "/Start":
        bot.send_message(message.from_user.id, "Я простой калькулятор, у меня мало функций. Напиши или нажми на /Help, чтобы вызвать меню и посмотреть, что я могу.")
    
    elif message.text == "/Help":
        bot.send_message(message.from_user.id, "Вот, что я могу:\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Out, чтобы выйти из меню.")
    
    elif message.text == "/1_Sum":
        bot.send_message(message.from_user.id, f"Введите первое число.")
        bot.register_next_step_handler(message, sum1)
        # bot.send_message(message.from_user.id, "Что делать дальше?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Out, чтобы выйти из меню.")

    elif message.text == "/2_Sub":
        bot.send_message(message.from_user.id, f"Введите первое число.")
        bot.register_next_step_handler(message, sub1)

    elif message.text == "/3_Mult":
        bot.send_message(message.from_user.id, f'Введите первое число.')
        bot.register_next_step_handler(message, mult1)

    elif message.text == "/4_Div":
        bot.send_message(message.from_user.id, f'Введите первое число.')
        bot.register_next_step_handler(message, div1)

    elif message.text == "/5_Out":
        bot.send_message(message.from_user.id, f'Спасибо за визит, сообщи, если я буду полезен!')

    else:
        bot.send_message(message.from_user.id, "Привет, я тебя не понимаю. Напиши или нажми на /Start.")

def sum1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, sum2)

def sum2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} + {b} = {a + b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Out, чтобы выйти из меню.")

def sub1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, sub2)

def sub2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} - {b} = {a - b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Out, чтобы выйти из меню.")

def mult1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, mult2)

def mult2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} * {b} = {a * b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Out, чтобы выйти из меню.")

def div1(message):
    global a
    a = int(message.text)
    bot.send_message(message.from_user.id, f"Введите второе число")
    bot.register_next_step_handler(message, div2)

def div2(message):
    b = int(message.text)
    bot.send_message(message.from_user.id, f"{a} / {b} = {a / b}\nПродолжим?\nВыбери /1_Sum, чтобы сложить два числа.\nВыбери /2_Sub, чтобы найти разницу двух чисел.\nВыбери /3_Mult, чтобы умножить два числа.\nВыбери /4_Div, чтобы разделить числа.\nВыберите /5_Out, чтобы выйти из меню.")

print("Server start")
bot.polling(none_stop=True, interval=0)