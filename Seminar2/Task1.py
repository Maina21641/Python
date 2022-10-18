# Напишите программу, которая принимает на вход число N и выдает последовательность из N членов.
import random
N = int(input("Enter namber N: "))
print(f"For N = {N}: ", end= '')
arr = []
for i in range(N):
    arr.append(random.randint(-100, 100))
print(arr)