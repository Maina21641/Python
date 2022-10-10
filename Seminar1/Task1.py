# Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
# 1-й пример
N1 = int(input("Enter the first number: ")) # Вводим что-то с консоли и это что-то конвертируется в int
N2 = int(input("Enter the second number: "))
if (N2 == N1 * N1) or (N1 == N2 *N2):
    print ("Yes")
else:
    print("No")
# 2-й пример
N1 = int(input("Enter the first number: ")) # Вводим что-то с консоли и это что-то конвертируется в int
N2 = int(input("Enter the second number: "))
if (N2 == N1 * N1):
    print ("Yes")
elif(N1 == N2 *N2):
    print("Yes")
else:
    print("No")