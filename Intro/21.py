print("hej.")
print("Spelarna väljer ett nummer varannan tur och den som når 21 vinner.")
print("Du kan inte ta samma nummer i rad.")
print("Om en spelare går över 21 vinner den andra.")

Number_21 = 0

Last_picked_1 = None
Last_picked_2 = None

while True:

    Player_1_number = int(input("Spelare 1: "))
    if Player_1_number == Last_picked_1:
        print("Du kan inte ta samma nummer två gånger i rad")
        continue
    if Player_1_number == 1:
        Number_21 += Player_1_number
        print(f"21 : {Number_21}")
        Last_picked_1 = Player_1_number
        if Number_21 == 21:
            print("Spelare 1 har vunnit!")
            break
    elif Player_1_number == 2:
        Number_21 += Player_1_number
        print(f"21 : {Number_21}")
        Last_picked_1 = Player_1_number
        if Number_21 == 21:
            print("Spelare 1 har vunnit!")
            break
        elif Number_21 >= 21:
            print("Spelare 2 har vunnit")
            break
    else:
        print("Du kan bara välja mellan siffrorna 1 - 2.")
        continue

    Player_2_number = int(input("Spelare 2: "))
    if Player_2_number == Last_picked_2:
        print("Du kan inte ta samma nummer två gånger i rad.")
        continue
    if Player_2_number == 1:
        Number_21 += Player_2_number
        print(f"21 : {Number_21}")
        Last_picked_2 = Player_2_number
        if Number_21 == 21:
            print("Spelare 2 har vunnit!")
            break
    elif Player_2_number == 2:
        Number_21 += Player_2_number
        print(f"21 : {Number_21}")
        Last_picked_2 = Player_2_number             #koden repeatar från spelare 1 och inte spelare 2 efter den sista continue.
        if Number_21 == 21:                         #koden hade sett mycket bättre ut och fungerat bättre om jag använt
            print("Spelare 2 har vunnit!")          #en while True: loop inom min while True: loop som milo viberg gjorde
            break                                   #men jag pallar inte att ändra detta och samtidigt är det ända som inte funkar
        elif Number_21 >= 21:                       #den sista continue
            print("Spelare 1 har vunnit")
            break
    else:
            print("Du kan bara välja mellan siffrorna 1 - 2.")
            continue    