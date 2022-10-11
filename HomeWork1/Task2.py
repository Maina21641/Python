# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# На сайте доказано https://spisok-literaturi.ru/postroenie-tablitciy-istinnosty-sknf-sdnf/function_451a20fe.html
# В совершенной конъюнктивной таблице истинности нет набора значений трех переменных X, Y, Z при которых функция ложна!
# В совершенной дизъюнктивной таблице истинности все значения (F) функций ¬X ∧ ¬Y ∧ ¬Z также истинны.
# Остается доказать это программно.
# X Y Z F Вывод
# 0 0 0 1=True
# 0 0 1 1=True
# 0 1 0 1=True
# 0 1 1 1=True
# 1 0 0 1=True
# 1 0 1 1=True
# 1 1 0 1=True
# 1 1 1 1=True

#1
for X in range(2):
        for Y in range(2):
            for Z in range(2):
                print(X, Y, Z, not (X or Y or Z) == (not X and not Y and not Z))

# 2
# def variables(x, y, z):
#     print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z) # если закомментить эту строку и посмотреть результат, прога выведет только первую строку и напечатает что утверждение Ложно
# if (variables(0, 0, 0) and variables(0, 0, 1) and variables(0, 1, 0) and variables(0, 1, 1) and variables(1, 0, 0) and variables(1, 0, 1) and variables(1, 1, 0) and variables(1, 1, 1)):
#     print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z Истинно")
# else:
#     print("Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z Ложно")