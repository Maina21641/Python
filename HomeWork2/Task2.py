# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

#1 вариант
number = input("Enter your integer number: ")

def MultiplyDigits(number):
    result=1
    for i in range(1, number+1):
        result=result*i
        print(result)

mineNumber=int(number)
MultiplyDigits(mineNumber)

#2 вариант
number = int(input("Введите число: "))
# number = 4
sum = 1
per = 1
while per <= number:
 sum = sum * per
 per = per + 1
 print(sum)