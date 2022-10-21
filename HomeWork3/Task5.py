# Task5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Негафибоначчи
#  Пример:
# для num = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = 8
fibonacci = [0, 1]
for i in range(1, num):
    fibonacci.append(fibonacci[i] + fibonacci[i-1])
negafibonacci = fibonacci
for j in range(num):
    negafibonacci.insert(0, (negafibonacci[1] - negafibonacci[0]))
print(negafibonacci)