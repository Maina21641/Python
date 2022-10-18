# 1. Получить список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200. Выполнить только при первом вхождении числа 20.

import random
N = 20
list1 = []
for i in range(N):
    list1.append(random.randint(15, 21))
print(list1)
for i in range(len(list1)):
    if list1[i] == 20:
        list1[i] = 200
        break
print(list1)

# 2. Получить список чисел. Превратите его в список квадратов этих чисел.

for i in range(len(list1)):
    list1[i] = list1[i] * list1[i]
print(list1)