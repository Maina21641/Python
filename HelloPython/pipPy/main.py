from telegram import Update
from telegram.ext import *
from bot_commands import *

app = ApplicationBuilder().token("5981406390:AAH-ywFKZArLDArOfGAXI0yroiy8qw-FLi8").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("1_Print_all_base", print_all_to_console))
app.add_handler(CommandHandler("2_Search_entry", search_entry))
app.add_handler(CommandHandler("3_Edit_entry", edit_entry))

print("Server start")
app.run_polling()
