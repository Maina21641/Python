# 3. Создайте программу для игры в "Крестики-нолики".
# создание поля
field = [["."]*3 for i in range(3)]
def make_field():
    # print("\n" * 10)
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end=' ')
        print() # после каждых трех точек отступ с красной строки

def step():
    while True:
        position = input("Введите два числа, через пробел, отвечающие за координаты игрового поля: ").split()
        
        x, y = position

        x, y = int(x), int(y)

        if field[x - 1][y - 1] != ".":
            print("Здесь значение уже есть")
            continue

        return x, y

def check():
    winner = [((0, 0), (0, 1), (0, 2)), 
    ((0, 0), (1, 1), (2, 2)), 
    ((0, 2), (1, 1), (2, 0)), 
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)), 
    ((0, 0), (1, 0), (2, 0)), 
    ((0, 1), (1, 1), (2, 1)), 
    ((0, 2), (1, 2), (2, 2))]
    for cord in winner:
        a, b, v = cord[0],cord[1],cord[2]
        if field[a[0]][a[1]]==field[b[0]][b[1]]==field[v[0]][v[1]]!=".":
            make_field()
            print(f"Победили {field[a[0]][a[1]]}!")
            return True
    return False

count = 0

while True:
    count += 1
    make_field()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x, y = step()

    if count % 2 == 1:
        field[x - 1][y - 1] = "X"
    else:
        field[x - 1][y - 1] = "0"

    if check():
        break

    if count == 9:
        print("Никто не победил")
        break