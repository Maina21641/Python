# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
# Пример:
# Для str_1 = ‘abcERDabcabc’
#        str_2 = ‘abc’
#       n = 3

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# count = 0
# for i in range(len(str1)-2):
#     if str1[i:i+len(str2)] == str2:
#         count = count+1
# print("n = ", count)

# Вариант от преподавателя

a = input()
b = input()
c=a.count(b)
print(c)