# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
#  Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
min = 0.0
max = 0.0

for i in range(len(list)):
    temp = float(list[i])
    temp %= 1
    if temp > max:
        max = temp
    elif temp < min:
        min = temp
result = int((max - min) * 100) / 100
print(result)