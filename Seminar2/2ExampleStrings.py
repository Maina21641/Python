# Написать программу, которая на основе заданной строки вида ХХХ выводит на экран “стихотворение” :
# ХХХХХХХХХХХХ
# ХХХХХХХХХ
# ХХХХХХ
# ХХХ

print(f"Enter string: ")
text = input()
print(f'{text * 4}\n{text * 3}\n{text * 2}\n{text}\n')