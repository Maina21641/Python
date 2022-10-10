# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Эту страшную вещь сделаль я!!!
# N1 = int(input("Enter the first number: "))
# N2 = int(input("Enter the second number: "))
# N3 = int(input("Enter the third number: "))
# N4 = int(input("Enter the fourth number: "))
# N5 = int(input("Enter the fifth number: "))
# # Как можно 5 строк ввода объединить в одну и как решить условие через метод?
# if (N1 > N2) and (N1 > N3) and (N1 > N4) and (N1 > N5):
#     print('Maximum is')
#     print(N1)
# elif (N2 > N1) and (N2 > N3) and (N2 > N4) and (N2 > N5):
#     print('Maximum is')
#     print(N2)
# elif (N3 > N1) and (N3 > N2) and (N3 > N4) and (N3 > N5):
#     print('Maximum is')
#     print(N3)
# elif (N4 > N1) and (N4 > N3) and (N4 > N2) and (N4 > N5):
#     print('Maximum is')
#     print(N4)
# elif (N5 > N1) and (N5 > N3) and (N5 > N4) and (N5 > N2):
#     print('Maximum is')
#     print(N5)
# Как в принте вывести и текст и переменую числовую?

# Решение на семинаре

max = int(input('Enter 1 number: ')) # присваиваем максимуму введенное первое число (чтобы оно могло быть и положительным и отрицательным)
for i in range(4): # Создаем цикл из пяти повторений (начинается с нуля)
    i+=1 # Нужно чтобы вторая строка опять не началась с 1-цы (словами преподавателя for не прибавляет счетчик, а присваивает значение)
    N = int(input(f'Enter {i+1} number: ')) # i+1 нужен чтобы при цвеличении счетчика его номер выводился в терминале
    if N > max: # Если число больше максимума
        max = N # Присваиваем максимуму это число
print(max) 