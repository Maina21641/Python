# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 11223
# print(type(value))

# переменная type показываем в терминале класс переменной в скобках

# s = ('hello world')
# print(s) # вывод строки
# print(a,b,s)
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}' .format (a, b, s)) # инедксы с 0

# в языке можно смешивать типы

# col = [1, 2, 3, 'hello']
# print(col)

# ввод и вывод

# print ('Введите a')
# a = int(input())
# print ('Введите b')
# b = int(input())
# print(a, ' + ' , b, ' = ' , a+b)

# print ('{} {}' .format(a, b))
# print (f'{a} {b}')2

# +, -,*, /, %, //,**
# **, ⊕, ⊖,*, /, //, %, +, -
# ( ), Сокращенные операции
# // - это деление в целых числах
# ** - возведение в степень

# a = 1.3213535254
# b = 3
# c = round(a * b, 7)
# print(c)

# Управляющие конструкции: if, if-else

# username = input('Введите имя: ')
# if username == 'Маша':
#  print('Ура, это же МАША!')
# elif username == 'Марина':
#  print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#  print('Ильнар - топ)')
# else:
#  print('Привет, ', username)

# Управляющие конструкции: while

# original = 23
# inverted = 0
# while original != 0:
#  inverted = inverted * 10 + (original % 10)
#  original //= 10
# print(inverted)

# Управляющие конструкции: for

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#         print(line)

# for i in range(0, 10, 2):
#     print(i)

# text = '333'
# print(text.isalpha())

# Функции

def f(x):
    if x == 1:
        return 'Целое' # print(type(f(arg))) = <class 'str'>
    elif x == 2.3:
        return 23      # print(type(f(arg))) = <class 'int'>
    else:
        return         # print(type(f(arg))) = <class 'NoneType'>
arg = 2.3 
print(type(f(arg)))