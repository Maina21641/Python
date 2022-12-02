# Файл для обновления информации, сразу после добавления нового контакта в файл Phonebook.txt
# Нужно для того, чтобы после добавления нового контакта, 
# можно было не только отобразить актуальную информацию в интерфейсе бота, но и чтобы скачать актуальный файл.

def GoToHtml():
    html = '<!DOCTYPE html>\n<html>\n  <head></head>\n  <body>\n    <h1>Телефонный справочник</h1>\n'
    with open('HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.txt', encoding = 'UTF-8') as data:
        for line in data.readlines():
            html += '   <p>' + line.removesuffix('\n') + '</p>\n'
    html += '  </body>\n</html>'
    with open('HomeWork9\\3PhoneBookBotTelegramm\\Phonebook.html', 'w', encoding='UTF-8') as data:
        data.write(html)
    return html