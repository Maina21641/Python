# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
with open('HomeWork4\\file1.txt','r') as f:
    s = str(f.readline())
print('Из первого файла прочитали многочлен:\n ',s)
with open('HomeWork4\\file2.txt','r') as f:
    v = str(f.readline())
print('Из второго файла прочитали другой многочлен: \n',v)
m = s + '+' + v
with open('HomeWork4\\file3.txt','w') as f:
    f.write(m)
print('В файл file3.txt записана сумма двух многочленов! \n', m)