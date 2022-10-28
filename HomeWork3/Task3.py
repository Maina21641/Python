# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
#  Пример:
# [0.1, 0.2, 0.1, 0, 0.01] => 0.19

list = [1.1, -1.3, 3.1, 5.1, 10.01]
max = 0.1
min = 0.1
for i in range(len(list)):
    temp = float(list[i])
    temp %= 1
    if temp > max:
        max = temp
        print(max)
    elif temp < min:
        min = temp
print(max)
print(min)
result = int((max - min) * 100) / 100
print(result)