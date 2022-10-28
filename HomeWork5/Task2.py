# 2. Создайте программу для игры с конфетами человек против человека.
#  Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#  a) Добавьте игру против бота
#  b) Подумайте как наделить бота "интеллектом"

from random import randint

def step(name):
    x = int(input(f"{name}, введите количество конфет, которое вы возьмете, от 1 до 28: "))
    print()
    while x < 1 or x > 28:
        x = int(input(f"{name}, не жульничайте, введите другое количество конфет, от 1 до 28: "))
    return x

def message(name, candy, size, totalSize):
    print(f"Ходил(а) {name}, взял(а) {candy} конфет, теперь у игрока {size} конфет. Осталось {totalSize} конфет в розыгрыше.")
    print()

def bot(totalSize):
    candy = randint(1,29)
    while totalSize-candy <= 28 and totalSize > 29:
        candy = randint(1,29)
    return candy

player1 = input("Напишите ваше имя: ")
print()
player2 = "Bot"
totalSize = 100 #int(input("Введите количество конфет на столе: "))
print(f"Разыгрывается {totalSize} конфет, выиграет и заберет все конфеты тот, кто сделает последний ход.")
print()
draw = randint(0,2) # жеребьевка
if draw:
    print(f"Первый ходит {player1}.")
    print()
else:
    print(f"Первый ходит {player2}.")
    print()

size1 = 0
size2 = 0

while totalSize > 28:
    if draw:
        candy = step(player1)
        size1 += candy
        totalSize -= candy
        draw = False
        message(player1, candy, size1, totalSize)
    else:
        candy = bot(totalSize)
        size2 += candy
        totalSize -= candy
        draw = True
        message(player2, candy, size2, totalSize)

if draw:
    print(f"{player1} выиграл(а) и забирает все конфеты!")
else:
    print(f"{player1} выиграл(а) и забирает все конфеты!")