def InterfaceMenu():
    print("Что можно сделать:\n \
           1 - импортировать новые данные\n \
           2 - экспортировать справочник в формате html\n \
           3 - экспортировать справочник в формате csv")

def Item():
    ItemUser = input("Выберите номер действия: ")
    return ItemUser

def Record():
    name = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    line = (f"{name}: телефон {phone}")
    return line