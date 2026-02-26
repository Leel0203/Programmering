shop = {
    "äpple" : {"price" : 5, "amount" : 10},
    "mjölk" : {"price" : 10, "amount" : 20},
    "chips" : {"price" : 15, "amount" : 15}
}

historik = []  #fastnade lite på hur man gjorde den här delen utan att göra en ny lista :shrug:

sales = [] #det är därför vi har sales och sales_money istället för bara sales

print("Välkommen till Butikshanteraren 3000")
print('Inloggad som Butiksägare')

while True:
    print("Vad vill du göra?")
    print("1. Visa alla varor")
    print("2. Lägg till en ny vara")
    print("3. Ändra priset på vara")
    print("4. Fylla på vara")
    print("5. Sälja en vara")
    print("6. Visa total intäkter")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        pass
        for item, dict_in_the_dict in shop.items():
            print(item.ljust(2), dict_in_the_dict["price"], "kr", dict_in_the_dict["amount"], "st")
    elif choice == "2":
        pass
        print("vad vill du lägga till?")
        lägga_till = input()
        print("vad är priset av denna vara?")
        lägga_till_pris = int(input())
        print("Hur många finns det av denna vara på lagret?")
        lägga_till_lager = int(input())
        shop[lägga_till] = {"price" : lägga_till_pris, "amount" : lägga_till_lager}
        historik.append({"name" : lägga_till, "price" : lägga_till_pris, "amount" : lägga_till_lager})
    elif choice == "3":
        pass
        print("Vilken vara vill du byta pris på?")
        byta_vara = input()
        if byta_vara in shop:
            print("Vad vill du att varan ska kosta?")
            byta_pris = int(input())
            shop[byta_vara] = {"price" : byta_pris, "amount" : shop[byta_vara]["amount"]}
            historik.append({"name" : byta_vara, "price" : byta_pris, "amount" : shop[byta_vara]["amount"]})
        else:
            print("Varan finns inte i systemet.")
    elif choice == "4":
        pass
        print("Namn på varan?")
        lager_vara = input()
        if lager_vara in shop:
            print("Hur många av varan fylls på?")
            lager_fylls_på = int(input())
            shop[lager_vara]["amount"] += lager_fylls_på
            historik.append({"name" : lager_vara, "price" : shop[lager_vara]["price"], "amount" : shop[lager_vara]["amount"]})
            print(historik)#holy shit kodan ovan funkar, satt med den i typ 30 minuter :sob:
        else:
            print("Varan finns inte i vårat system.")
    elif choice == "5":
        pass
        print("Vilken vara har det sålts av?")
        vara_sold = input()
        print("Hur många av denna vara har sålts?")
        vara_sold_antal = int(input())
        shop[vara_sold]["amount"] -= vara_sold_antal
        if shop[vara_sold]["amount"] == 0:                          
            print("Varan tas bort från lagret")  
            historik.append({"name" : vara_sold, "price" : shop[vara_sold]["price"], "amount" : shop[vara_sold]["amount"]})                              
            sales.append(shop[vara_sold]["price"] * vara_sold_antal)       
            shop.pop(vara_sold)
        elif shop[vara_sold]["amount"] > 0:    
            historik.append({"name" : vara_sold, "price" : shop[vara_sold]["price"], "amount" : shop[vara_sold]["amount"]})
            sales.append(shop[vara_sold]["price"] * vara_sold_antal)       
            print("Varan finns kvar på lagret fast i mindre antal.")
        elif shop[vara_sold]["amount"] < 0:
            print("Det finns inte nog med varan på lagret för att sälja såhär många.")
            shop[vara_sold]["amount"] += vara_sold_antal 
        else:                                   
            ("Din kod suger balle.")            
    elif choice == "6":                         
        pass  
        print("Här är historiken / transaktionerna: ")
        print(historik)    #osäker om den här delen var nödvändig eller inte :shrug:
        print("Här är transaktionerna:", sales)  #det står inte i kronor, men jag tänker anta att man förstår vad siffrorna betyder, annars har man ju också historiken ovan där man kan see alla förändringar                   
        print("Totala intäkten:", sum(sales), "kr.")
    elif choice == "q":
        break
    else:
        print("Ogiltigt Svar")
    
    input("\nTryck enter för att fortsätta...")