import time

print("Du står framför en bankomat")
print("Men först, hur mycket pengar har du?")

konto = int(input())

konto_2 = [konto] 
     
while True: 
    print("Du ser 3 alternativ framför dig.")
    print("1. Visa saldo / historik")
    print("2. Ta ut pengar")
    print("3. Sätta in pengar")

    choice = int(input())

    if choice == 1:
        print("Du har", konto, "kr.")
        print(konto_2)
        time.sleep(2)
    elif choice == 2:
       print("Hur mycket pengar vill du ta ut?")
       pengar_minus = int(input())
       konto_minus_pengar = konto - pengar_minus
       konto = konto_minus_pengar
       print("Okej, du har tagit ut", pengar_minus, "kr.")
       print("Och du har", konto_minus_pengar, "kr kvar på kontot.")
       konto_2.append(konto_minus_pengar) #inte helt rätt, visar inte + - bara totalt
       time.sleep(2)
    elif choice == 3:
        print("Hur mycket vill du sätta in?")
        pengar_in = int(input())
        konto_plus_pengar = konto + pengar_in
        konto = konto_plus_pengar
        print("Okej, du har nu ", konto_plus_pengar, "kr på kontot.")
        konto_2.append(konto_plus_pengar)
        time.sleep(2)
    else:
        print("Du går därifrån istället.")
        break