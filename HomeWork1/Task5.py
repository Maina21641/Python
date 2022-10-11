# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

#AB = Корень (xb - xa)^2 + (yb - ya)^2 // формула нахождения длинны вектора

import math

xa = int(input("Enter number coordinate xa: "))
ya = int(input("Enter number coordinate ya: "))
xb = int(input("Enter number coordinate xb: "))
yb = int(input("Enter number coordinate yb: "))

print(round(math.sqrt(math.pow((xb - xa), 2) + math.pow ((yb - ya), 2)), 3))

# при примере с координатами - A (7,-5); B (1,-1) выдает правильный резаультат 7,21
# а при - A (3,6); B (2,1) выдает 5,1 при округлении до двух чисел после ноля 
# или 5,099 при округлении до 3-х чисел после нуля вместо 5,09 указанных в примере