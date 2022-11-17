def GoToHtml():
    html = '<!DOCTYPE html>\n<html>\n  <head></head>\n  <body>\n    <h1>Телефонный справочник</h1>\n'
    with open('HomeWork7\\PhoneDirectory\\Phonebook.txt', encoding = 'UTF-8') as data:
        for line in data.readlines():
            html += '   <p>' + line.removesuffix('\n') + '</p>\n'
    html += '  </body>\n</html>'
    with open('HomeWork7\\PhoneDirectory\\Phonebook.html', 'w', encoding='UTF-8') as data:
        data.write(html)
    return html