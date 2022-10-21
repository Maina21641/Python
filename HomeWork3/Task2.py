# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#  Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# list = [2, 5, 7, 8]
#     #/ 2; // делим на 2, чтобы дойти до середины, чтобы не было дубликатов произведений
# newlist = 0
# for i in range(len(list)//2):
#     newlist[i] = list[i] * list[len(list) - 1 - i]
# print(newlist)

# def composition():
#     list = [2, 3, 5, 6]
#     new_array = [list[i] * list[0 - i - 1] for i in range(len(list) // 2)]
#     print(new_array)

# composition()

# list = [2, 3, 5, 6]
# for i in range(len(list) // 2):
#     new_array = list[i] * list[0 - i - 1]
#     print(new_array)

# def composition():
#     list = [2, 3, 5, 5, 6]
#     new_array = [list[i] * list[0 - i - 1] for i in range(len(list) // 2 +1)]
#     print(new_array)

# composition()

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
def multy(pair): 
    result = [] 
    for i in range(len(pair)):
        if(i <= len(pair) - i - 1): 
            result.append(pair[i] * pair[len(pair) - i - 1])
    return result
print(f'Произведение пар списка - {list1} = {multy(list1)}')
print(f'Произведение пар списка - {list2} = {multy(list2)}')