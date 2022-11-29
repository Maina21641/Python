# def reading():
#     contacts = [0] * 4
#     contacts[0] = input("Введите фамилию: ")
#     contacts[1] = input("Введите имя: ")
#     contacts[2] = input("Введите Телефон: ")
#     contacts[3] = input("Введите описание: ")
#     return contacts

def newstring(contacts):
    bazaopen = open("HomeWork8\\employees.csv", "a", encoding = 'utf-8')
    bazaopen.write('\n' + f"{contacts[0]},")
    bazaopen.write(f" {contacts[1]}, ")
    bazaopen.write(f" {contacts[2]}, ")
    bazaopen.write(f" {contacts[3]}, ")
    bazaopen.write(f" {contacts[4]}, ")
    bazaopen.write(f" {contacts[5]}; ")
    bazaopen.close()