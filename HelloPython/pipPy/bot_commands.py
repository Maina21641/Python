import time
from telegram import Update
from telegram.ext import *
import datetime

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
  
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/1_Print_all_base\n/2_Search_entry\n/3_Edit_entry')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    await update.message.reply_text(f'hi {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def print_all_to_console(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('HelloPython\\pipPy\\employees.csv', encoding="utf-8") as data:
        for line in data:
            await update.message.reply_text(line.replace(',', ' '))

async def search_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Введите команду /2_Search_entry и далее, через пробел, элемент для поиска сотрудника в БД. Например: /2_Search_entry Петр')
    # по поиску /2_Search_entry Петр - бот выдаст:
    # 1, Сологуб, Иван, Петрович, +71231231212, Бухгалтерия, Экономист;
    # 2, Петров, Гоша, Сергеевич, +7(912)472-22-12, Бухгалтерия, Главный бухгалтер;
    # 4, Иванов, Петр, Васильевич, +7-966-666-55-44, Закупки, Человек;
    name = update.message.text
    print(name)
    items = name.split()
    x = (items[1])
    
    with open('HelloPython\\pipPy\\employees.csv', 'r', encoding="utf-8") as data:
            for line in data:
                if x in line:
                    await update.message.reply_text(line.replace(',', ' '))

async def edit_entry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Введите элемент имя сотрудника для изменения данных о нём в БД: ')
        
        name = update.message.text
        print(name)
        lines = []
        items = name.split()
        x = (items[1])

        with open('HelloPython\\pipPy\\employees.csv', 'r', encoding="utf-8") as data:
                for line in data:
                    if not x in line: 
                        lines += line
                    else:
                        line = line.split(", ")
                        print(line)
                        # old = int(input("Укажите номер элемента (1-5) для замены: "))
                        old = int(await update.message.reply_text(f"Укажите номер элемента (1-7) для замены: "))
                        time.sleep(10)
                        new = await update.message.reply_text(f"На что заменить: ")
                        time.sleep(10)
                        line[old - 1] = new
                        line = ", ".join(line)
                        lines += line

        with open('HelloPython\\pipPy\\employees.csv', 'w', encoding="utf-8") as data:
                data.writelines(lines)
        await update.message.reply_text('Изменение произведено...')