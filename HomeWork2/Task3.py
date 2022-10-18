# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n= int(input('введите число '))
# set_list={}
# sum=0
# for i in range(1,n+1):
#     set_list[i] = (1+1/i)**i
#     sum+=set_list[i]
# #sum=round(sum,3)
# print(sum)
# print(set_list)

# n = int(input())
# lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')

n = int(input('Enter number: ')) 

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))))

# number = int(input("Введите количество чисел в списке: "))
# sum = 0
# d = {i : 3*i + 1 for i in range(1,number+1)}
# print(f"Для n = {number}: {d}")

# def sequence(number):
#     return[round((1 + 1 / i)i, 2) for i in range (1, number + 1)]          
# print(f'Список для {number} чисел =',sequence(number))

# for i in range(1, number + 1):
#     sum += (1 + 1 / i) ** i
# print(f'Сумма последовательности из {number} чисел равна: {sum}')