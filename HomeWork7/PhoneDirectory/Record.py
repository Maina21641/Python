def NewRecord(line):
    with open('HomeWork7\\PhoneDirectory\\Phonebook.txt', 'a', encoding = 'UTF-8') as data:
        data.write(f"\n{line}")
    with open('HomeWork7\\PhoneDirectory\\Phonebook.csv', 'a', encoding = 'UTF-8') as data:
        data.write(f"\n{line}")