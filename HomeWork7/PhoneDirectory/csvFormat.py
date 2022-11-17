import csv
def GoToCsv():
    with open('HomeWork7\\PhoneDirectory\\Phonebook.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open('HomeWork7\\PhoneDirectory\\Phonebook.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerows(lines)