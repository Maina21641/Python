#  Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = random.randint(1,10)
# k = 2
print('Натуральная степень k:', k)
spi =[]
for i in range(k):
    spi.append(random.randint(1, 100))
print('Список коэфициентов : \n ',spi)
s =str('')
for i in reversed(range(k)):
    if i == 0: s = s + '+' +  str(spi[i])
    elif i == 1: s = s + str(spi[i]) + '*x'
    else: 
        s = s + str(spi[i])+ '*x**' + str(i) + '+'

print('Сформирован многочлен: \n',s)
with open('HomeWork4\\TextforTask4.txt','w') as f:
    f.write(s)