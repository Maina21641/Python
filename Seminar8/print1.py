def print_all_to_console():
    with open('Seminar8\\employees.csv', encoding="utf-8") as data:
        for line in data:
            print(line.replace(',', ' '))