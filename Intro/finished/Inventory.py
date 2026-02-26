backpack = ["Morot", "Yxa", "Tacos", "Haj"]

while True:
    print("Vad vill du göra?")
    print("1. Visa Ryggsäcken")
    print("2. Plocka upp något")
    print("3. Släppa något i ryggsäcken")
    print("4. Byta plats i ryggsäcken")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        for list in backpack:
            print(list)
    elif choice == "2":
        print("Vad vill du lägga till?")
        lägga_till = input()
        backpack.append(lägga_till)
    elif choice == "3":
        print("Vad vill du ta ur ryggsäcken?")
        ta_ut = input()
        if ta_ut in backpack: #Try except fungerar också
           backpack.remove(ta_ut)
        else:
            print("Hittade inte i ryggsäcken.")
    elif choice == "4":
        print("Vad vill du byta plats på i ryggsäcken?")
        print(backpack)
        print("Objekt 1: ")
        Objekt_1 = int(input())
        print("Objekt 2: ")
        Objekt_2 = int(input())
        backpack[Objekt_1], backpack[Objekt_2] = backpack[Objekt_2], backpack[Objekt_1]
    elif choice == "q":
        break
    else:
        print("Ogiltigt Svar")
    input("\nTryck enter för att fortsätta...")