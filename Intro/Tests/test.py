dict = {
    "äpple" : {"price" : 5, "amount" : 10}
}

dict_2 = {
    
}

while True:

    choice = int(input(print("1 - 3:")))

    if choice == 1:
        pass
        for item, info in dict.items():
            print(item, info["price"], "kr", info["amount"], "st")
    elif choice == 2:
        pass
        hey = input("Ange en variable: ")
        hey_2 = int(input("Hur mycket adderas till denna variabel?"))
        dict[hey]["amount"] += hey_2
        dict_2[hey_2]
    elif choice == 3:
        pass
        hey_3 = input("Ange en variabel: ")
        hey_4 = int(input("Hur mycket tas bort från variabeln?"))
        dict[hey_3]["amount"] -= hey_4
        dict_2[hey_4]
    elif choice == 4:
        print(dict_2)
    else:
        print("kuk")
        break
        
    input("tryck för att börja igen type shi")