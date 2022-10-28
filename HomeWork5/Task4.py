# 4 задача. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример
# 	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E


# import os
# os.system("cls")    

# алгоритм сжатия
def compression(text):
    bit = ''
    previous = ''
    count = 1
   
    for i in text:
        if i != previous:
            if previous:
                bit += str(count) + previous
            count = 1
            previous = i
        else:
            count += 1
    else:
        bit += str(count) + previous
        return bit

# алгоритм восстановления
def deploy(text):
    result = ''
    count = ''
    for i in text:
        if i.isdigit():
            count += i
        else:
            result += i * int(count)
            count = ''
    return result

with open('HomeWork5\\1origin.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Напишите текст который нужно сжать (он будет помещен в файл 1origin.txt): '))
    
with open('HomeWork5\\1origin.txt', 'r') as file:
    origin = file.readline()
resultСomp = compression(origin)
print(f"Текст после сжатия '{resultСomp}' помещен в файл 2resultСomp.txt")

with open('HomeWork5\\2resultСomp.txt', 'w') as file:
    file.write(f'{resultСomp}')

with open('HomeWork5\\2resultСomp.txt', 'r') as file:
    back = file.readline()
originText = deploy(back)

with open('HomeWork5\\3backToOrigin.txt', 'w') as file:
    file.write(f'{originText}')

print(f"Текст после восстановления'{originText}' помещен в файл 3backToOrigin.txt")