# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Пример на вход
num = int(input('Введите натуральное число N: '))
list = []
for i in range(2, num +1):
    while num % i == 0 and i <= num: 
        list.append(i)
        num /= i
print(list)
# Пример с фиксированными числами
# def Multy(n):
#     simple = []
#     for i in range(2, n):
#         for j in range(2, i + 1):
#             if (i % j == 0) and (i != j):
#                 break
#             if i == j:
#                 simple.append(j)
            
#     list = []
#     for i in simple:
#         if n % i == 0:
#             list.append(i)
#     return list

# n = 1463
# print(f"Список простых множителей числа {n} = {Multy(n)}")
# n = 66
# print(f"Список простых множителей числа {n} = {Multy(n)}")
# n = 6441
# print(f"Список простых множителей числа {n} = {Multy(n)}")