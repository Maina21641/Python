#1 вариант кода на создаине файла и добавление в него данных

# colors = ['red', 'green', 'blue'] # данные
# data = open('HelloPython\\file.txt', 'w') # HelloPython\\ указание пути создания файла
# # a = создает файл и добавляет данные
# # w = перезапись данных
# data.write(colors) # добавление строки от переменной с ее данными в массиве - 
# # разделителей не будет - будет redgreenblue
# # data.write(colors) - выдает ошибку
# data.writelines('\nline 123') # символ \n делает перенос данных с новой строки
# data.close() # нужно для закрытия кода

#2 вариант кода на создаине файла и добавление в него данных

# with open('HelloPython\\file.txt', 'w') as data:
#  data.write('line 1\n')
#  data.write('line 2\n')

# Код на чтение файла и вывод содержимого строк

# path = 'HelloPython\\file.txt'
# data = open(path, 'r') # 'r' - режим чтения
# for line in data:
#  print(line)
# data.close()

# Импорт ответа по функции из другого файла

# import hello
# print(hello.f(1))

# Умножение строки на число

# def new_string(symbol, count = 3):
#  return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# Склеивание строк против сложения чисел
# def concatenatio(*params): # * нужна для объявления множества любых аргументов
#  # res: str = "" 
#  res: int = 0
#  for item in params:
#     res += item
#  return res
# # print(concatenatio('a', 's', 'd', 'w')) # asdw
# # print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio(1, 2, 3, 4)) # 10

# Рекурсия

# def fib(n):
#  if n in [1, 2]:
#     return 1
#  else:
#     return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# Кортеж

# a = (1, 2, 31, 4)
# print(a[-2])
# a[0] = 12 # выдаст ошибку, так как список неизменен TypeError: 'tuple' object does not support item assignment

# Словари

# dictionary = {} # если нужен пустой словарь
# # если требуется указание каких-то пар пишем в фигурных скобках слева направление, справа значение через двоеточия
# dictionary = \
# {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
# }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться

