def int_checker(prompt):    
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ange en integer.")

number_1 = int_checker("Nummer 1: ")
number_2 = int_checker("Nummer 2: ")

for x in range(number_1, number_2):
    if x % 2 != 0:
        continue
    print(x)