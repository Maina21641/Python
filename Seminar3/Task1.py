# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# А) Реализовать создание списка случайных элементов
# Б) Реализовать создание списка случайных элементов - строк
# 1 вариант
# import datetime
# a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# #print(a)
# a = a%1
# print(round(a, 6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# #print(a)
# a = a%1
# print(round(a, 6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# #print(a)
# a = a%1
# print(round(a, 6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# #print(a)
# a = a%1
# print(round(a, 6))
# a *= (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# #print(a)
# a = a%1
# print(round(a, 6))

# 2 вариант

# import datetime
# b1=10
# b2=20
# a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
# a = a%1
# new=round(b1+(b2-b1)*a)
# print(new)

# 3 вариант c буквами
import datetime
mas = list(map(chr, range(97, 123)))
print(mas)
n=15
b1=0
b2=25
a = (datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
a=a%1
s=''
for i in range (5):
    a = a*(datetime.datetime.now() - datetime.datetime(1, 1, 1, 0, 0)).total_seconds()
    a=(a*1000)%1
    #sleep(1)
    print(a)
    stroka=mas[round(b1+(b2-b1)*a)]
    s+=stroka
print(s) 