# Улучшение кода для уже решённых задач:

# HomeWork3. Task2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# было
# list1 = [2, 3, 4, 5, 6]
# list2 = [2, 3, 5, 6]
# def multy(pair): 
#     result = [] 
#     for i in range(len(pair)):
#         if(i <= len(pair) - i - 1): 
#             result.append(pair[i] * pair[len(pair) - i - 1])
#     return result
# print(f'Произведение пар списка - {list1} = {multy(list1)}')
# print(f'Произведение пар списка - {list2} = {multy(list2)}')

# с помощью List comprehension стало
# list1 = [2, 3, 4, 5, 6]
# print (list1)
# list2 = [(list1[i]*list1[len(list1)-1-i]) for i in range((len(list1)+1)//2)]
# print(list2)

# HomeWork3. Task1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# было
# list = [2, 3, 5, 9, 3] 
# print(list) 
# sum = 0
# for i in range(len(list)):
#      if i %  2 != 0:
#          sum = sum + list[i]
# print(f'Сумма элементов, находящихся на нечётной позиции = {sum}' )

#стало
# list = [2, 3, 5, 9, 3] 
# new_list = [x for i, x in enumerate(list) if i % 2 != 0] 
# print(f'Элементы на нечетных позициях {new_list}, а их сумма равна {sum(new_list)}')

# HomeWork2. Task1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# было
# number = input("Введите вещественное число: ")
# sum = 0
# for i in number:
#     if i != '.':
#         sum += int(i)
# print(sum)

#стало
# number = lambda x: sum([int(it) for it in str(x) if "0" <= it <= "9"])
# print(number(-6782))