# Напишите программу, которая принимает на вход число и проверяет, 
# кратно ли оно 5 и 10 или 15, но не на 30

a =float (input("Enter number: "))
if ( a % 5 == 0 and a % 10 == 0 or a % 15 == 0 ) and a % 30!=0:
    print ("True")
else:
    print ("False")