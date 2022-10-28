#1 Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = list('Алфавит начинается с абв'.split())
print(text)
for i in text:
    if 'абв' not in i:
        print(i, end=' ')