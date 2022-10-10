# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

N = int(input('Enter number N: '))
N = abs(N) # абсолютное значение - любое число без минуса
# через for
# for i in range(-N, N+1):
#     print(i)
# через цикл
i = -N
while i < N:
    print(i)
    i += 1
print(N)