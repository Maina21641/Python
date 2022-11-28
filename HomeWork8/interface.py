import delete
import print1
import edit
import search

while True:
    print("База данных сотрудников.\n")
    print('1. Вывести все записи.\n3. Найти запись.\n4. Изменить запись.\n5. Удалить запись.\n6. Выход.\n')

    value = int(input("Выберите действие: "))
    # print(value)
    if value == 1:
        print1.print_all_to_console()
    # elif value == 2:
    #     # add.reading
    #     write.New_Entry
    elif value == 3:
        search.Search_Entry('HomeWork8\\employees.csv')
    elif value == 4:
        edit.Edit_Entry('HomeWork8\\employees.csv')
    elif value == 5:
        delete.delete_str('HomeWork8\\employees.csv')
    elif value == 6:
        break