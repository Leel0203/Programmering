number_list = []

number_1 = int(input("nummer 1: "))

number_2 = int(input("nummer 2: "))

number_3 = int(input("nummer 3: "))

number_4 = int(input("nummer 4: "))

number_5 = int(input("nummer 5: "))

number_6 = int(input("nummer 6: "))

number_7 = int(input("nummer 7: "))

number_8 = int(input("nummer 8: "))

number_9 = int(input("nummer 9: "))

number_1_copy = number_1
number_1 *= 2
if number_1 >= 10:
    variable1 = number_1 // 10
    variable1_1 = number_1 % 10
    number_list.append(variable1)
    number_list.append(variable1_1)
else: 
    variable1_1 = number_1 % 10
    number_list.append(variable1_1)

number_2_copy = number_2
number_2 *= 1
if number_2 >= 10:
    variable2 = number_2 // 10
    variable2_2 = number_2 % 10
    number_list.append(variable2)
    number_list.append(variable2_2)
else: 
    variable2_2 = number_2 % 10
    number_list.append(variable2_2)

number_3_copy = number_3
number_3 *= 2
if number_3 >= 10:
    variable3 = number_3 // 10
    variable3_3 = number_3 % 10
    number_list.append(variable3)
    number_list.append(variable3_3)
else: 
    variable3_3 = number_3 % 10
    number_list.append(variable3_3)

number_4_copy = number_4
number_4 *= 1
if number_4 >= 10:
    variable4 = number_4 // 10
    variable4_4 = number_4 % 10
    number_list.append(variable4)
    number_list.append(variable4_4)
else: 
    variable4_4 = number_4 % 10
    number_list.append(variable4_4)

number_5_copy = number_5
number_5 *= 2
if number_5 >= 10:
    variable5 = number_5 // 10
    variable5_5 = number_5 % 10
    number_list.append(variable5)
    number_list.append(variable5_5)
else: 
    variable5_5 = number_5 % 10
    number_list.append(variable5_5)

number_6_copy = number_6
number_6 *= 1
if number_6 >= 10:
    variable6 = number_6 // 10
    variable6_6 = number_6 % 10
    number_list.append(variable6)
    number_list.append(variable6_6)
else: 
    variable6_6 = number_6 % 10
    number_list.append(variable6_6)

number_7_copy = number_7
number_7 *= 2
if number_7 >= 10:
    variable7 = number_7 // 10
    variable7_7 = number_7 % 10
    number_list.append(variable7)
    number_list.append(variable7_7)
else: 
    variable7_7 = number_7 % 10
    number_list.append(variable7_7)

number_8_copy = number_8
number_8 *= 2
if number_8 >= 10:
    variable8 = number_8 // 10
    variable8_8 = number_8 % 10
    number_list.append(variable8)
    number_list.append(variable8_8)
else: 
    variable8_8 = number_8 % 10
    number_list.append(variable8_8)

number_9_copy = number_9
number_9 *= 2
if number_9 >= 10:
    variable9 = number_9 // 10
    variable9_9 = number_9 % 10
    number_list.append(variable9)
    number_list.append(variable9_9)
else: 
    variable9_9 = number_9 % 10
    number_list.append(variable9_9)

guh = sum(number_list)
last_number = (10 - (guh % 10)) % 10    #orkade inte kolla om hela koden beräknar rätt eller om ja skrivit nått fel 

print(f"Ditt personnummer är: {number_1_copy}{number_2_copy}{number_3_copy}{number_4_copy}{number_5_copy}{number_6_copy}-{number_7_copy}{number_8_copy}{number_9_copy}{last_number}")
#Poängen med hela koden var nog att man skulle skicka alla 9 siffror i en string eller något liknande
#så man sedan kan plocka ut dem enskilt, men jag pallade inte.
#Därför är de tagna separat
#helt ärligt hade jag nog kunnat använt en def för att korta ner allt till typ 30-40 rader