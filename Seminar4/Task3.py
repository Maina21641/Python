# Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.
# От Антона Кулакова
# a = 4
# b = 6
# for i in range(a, a*b*5):
#     if i % a ==0 and i % b ==0:
#         print(f'НОК = {i}')
#         break

# От Евгения
# def gin():
#     try:
#         user_input = int(input('Введите целое число '))
#         return user_input
#     except ValueError as v:
#         print(v)
#         return gin()
# n1 = int(input('Введите целое число '))
# n2 = int(input('Введите целое число '))
# a = True
# b = 1
# while a:
#     if (n1*b) % n2 == 0:
#         print(n1*b)
#         a = False
#     b += 1

# Код преподавателя
c = a =5214
d = b = 5831
while a !=0:
    b,a = a, b%a
print(int(c*d/b))