# lambda
# например, есть функция, которая складывает значения и мы ее используем один раз за код
# ее можно сократить и позднее использовать, конкретно там, где мы ее вызываем
# def sum (x, y):
#     return x+y
# аналогичная запись
# sum = lambda x, y: x+y
# помещаем эту сжатую версию в выводе кода
# def calc(op, a, b):
#     print(op(a, b))
# calc(lambda x, y: x+y, 4, 5)
# функция calc, внутри которой в виде аргумента другая функция

# Задача
# В листе хранятся числа, нужно выбрать четные и составить список пар (число; квадрат\куб числа).

# list = []
# for i in range(1, 20):
#     if(i%2 == 0):
#         list.append(i)
# print(list)

# Как это сократить и вставить там, где мы вызовем функцию?
# def f(x):
#     return x**3
# list = [(i, f(i)) for i in range(1, 21) if i%2 ==0]
# print(list)
# from importlib.resources import path

# еще пример (который можно сократить с помощью функций map() and filter())
# def select(f, col):
#     return[f(x) for x in col]
# def where(f, col):
#     return[x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# Список с первоначальными часлами выводим с прибавками
# li = [x for x in range(1, 20)]
# print(li)
# li = list(map(lambda x: x+10, li))
# print(li)

# Исключение map
# data = map(int, '1 2 3'.split())
# for e in data:
#     print(e)
# print('__')
# for e in data:
#     print(e)
# Второй раз работать с данными нельзя
# Нужно данные принудительно сохранить, Поэтому добавляем list
# data = list(map(int, '1 2 3'.split()))
# for e in data:
#     print(e)
# print('__')
# for e in data:
#     print(e)

# Наш пример (с функцией map() и filter())
# data = '1 2 3 5 8 15 23 38'.split()
# res = map(int, data)
# res = filter(lambda x: not x % 2, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

# Функция zip()
users = ['first', 'second', 'third', 'fourth', 'fifth']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids))
print(data)
# если количество элементов разное, выводится минимальный набор кортежей
data = list(zip(users, ids, salary))
print(data)