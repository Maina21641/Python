# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# numbers = [int (num) for num in input('Введите несколко чисел: ').split()]
# print(max(numbers))
# print(min(numbers))

#Ура! получилось!
list = [5, 10, 2, 11]
min = list[0]
max = list[0]
for i in list:
    if i > max:
        max = i
    elif i < min:
       min = i
print(min)
print(max)