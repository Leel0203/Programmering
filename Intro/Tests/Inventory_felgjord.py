Inventory = ["Yxa", "Sten", "Potatis"]

answer_1 = input("Vill du see inventariet?") #steg 1

if answer_1 == "ja" or answer_1 == "Ja":
    for answer_1 in Inventory:
        print(answer_1)
else:
    print("vafan")

answer_2 = input("Vill du lägga till något i listan?") #steg 2

if answer_2 == "ja" or answer_1 == "Ja":
    Hittade = input("Vad hittade du?")
    Inventory.append(Hittade)
    print(Inventory)
    while True:
        Hittade_mer = input("Hittade du något mer?")
        if Hittade_mer == "Ja" or Hittade_mer == "ja":
            Hittade_2 = input("Vad hittade du?")
            Inventory.append(Hittade_2)
        else:
            print("Okej.")
            break
    print("Inget läggs till.")

    answer_3 = input("Vill du ta bort något från inventariet?")
    if answer_3 == "Ja" or answer_3 == "ja":
        print(Inventory)
        Ta_bort = input("Vad vill du ta bort?")
        Inventory.remove(Ta_bort)
        print("Slängde", Ta_bort)
        while True:
            print(Inventory)
            Ta_bort_mer = input("Vill du ta bort något mer?")
            if Ta_bort_mer == "Ja" or Ta_bort_mer == "ja":
                Ta_bort_2 = input("Vad vill du ta bort?")
                Inventory.remove(Ta_bort_2)
                print("Slängde", Ta_bort_2)
            else:
                ("Inget mer tas bort.")
                break
        print("Inget tas bort.")

    answer_4 = input("Vill du byta plats på något i listan?")
    if answer_4 == "Ja" or answer_4 == "ja":
        print("Välj genom siffrorna 0 - slutet av listan.")
        print(Inventory)
        Objekt_1 = int(input("Första: "))
        Objekt_2 = int(input("Andra: "))
        Inventory[Objekt_1], Inventory[Objekt_2] = Inventory[Objekt_2], Inventory[Objekt_1]
        print(Inventory)
        print("GGs programmet är nu över och jag kan sova.")
    else:
        print("Du vill inte byta något i listan.")
        #Inte den vackraste koden, men den fungerar iaf