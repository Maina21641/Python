# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

list = [11, 11, 22, 33, 44, 44, 11, 55, 88, 88, 77]

# notRepeat = []
# for i in range(len(list)):
#     for j in range(len(list)):
#         if i != j and list[i] == list[j]:
#             break
#     else:
#         notRepeat.append(list[i])
# print(notRepeat)

print(tuple(filter(lambda num: list.count(num) == 1, list)))