import emoji

print(emoji.emojize(':thumbs_up:') * 10, " Игра Крестики-нолики ", emoji.emojize(':thumbs_up:') * 10)

pole = list(range(1,10))

def get_pole(pole):
   print("-" * 13)
   for i in range(3):
      print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|")
      print("-" * 13)

def get_input(request):
   valid = False
   while not valid:
      quest = input(f"Куда поставить {request}? ")
      try:
         quest = int(quest)
      except:
         print(emoji.emojize(':loudly_crying_face:'), "Вы ввели не число.")
         continue
      if quest >= 1 and quest <= 9:
         if(str(pole[quest-1]) not in "XO"):
            pole[quest-1] = request
            valid = True
         else:
            print("Позиция занята!", emoji.emojize(':loudly_crying_face:'))
      else:
         print("Введите число от 1 до 9.", emoji.emojize(':loudly_crying_face:'))

def win(pole):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if pole[each[0]] == pole[each[1]] == pole[each[2]]:
          return pole[each[0]]
   return False

def cells(pole):
    counter = 0
    win = False
    while not win:
      get_pole(pole)
      if counter % 2 == 0:
         get_input("X")
      else:
         get_input("O")
      counter += 1
      if counter > 4:
         tmp = win(pole)
         if tmp:
            print(tmp, "выиграл!")
            print(emoji.emojize(':clapping_hands:')* 10)
            win = True
            break
         if counter == 9:
            print("Ничья!", emoji.emojize(':loudly_crying_face:'))
            break
    get_pole(pole)
cells(pole)