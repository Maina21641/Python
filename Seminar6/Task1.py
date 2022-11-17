# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
#  Пример:
#  2+2 => 4;
#  1+2*3 => 7;
#  1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.
#  Пример:
#  1+2*3 => 7;
#  (1+2)*3 => 9;

# 1 вариант

formula = '22+2*3'
lst = []
numbers = ''

for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
print(lst)

for i in range(len(lst)-1, 0, -1):
    if lst[i] == '*':
        a = int(lst[i-1])*int(lst[i+1])
        lst[i-1] = a
        lst.pop(i+1)
        lst.pop(i)
        i-=1
    if lst[i] =='+':
        b = int(lst[i-1])+int(lst[i+1])
print(b)

# 2 вариант

formula = '24+2/2-30*3'
lst = []
numbers = ''

def Action(array,sign):
    i = 0
    while sign in array:
        if array[i] == sign:
            if sign == '/':
                a = int(array[i-1])/int(array[i+1])
            elif sign == '*':
                a = int(array[i-1])*int(array[i+1])
            elif sign == '-':
                a = int(array[i-1])-int(array[i+1])
            elif sign == '+':
                a = int(array[i-1])+int(array[i+1])
            array[i-1] = a
            array.pop(i+1)
            array.pop(i)
            i=0
        else:
            i+=1
    return(array)

for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
print(lst)

i = 0
while '*' in lst or '/' in lst:
    if lst[i] == '*':
        Action(lst,'*')
        i = 0
    elif lst[i] == '/':
        Action(lst,'/')
        i = 0
    else:
        i+=1
print(lst)

i = 0
while '-' in lst or '+' in lst:
    if lst[i] == '-':
        Action(lst,'-')
        i = 0
    elif lst[i] == '+':
        Action(lst,'+')
        i = 0
    else:
        i+=1
print(lst)