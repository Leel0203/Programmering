import time

zoo = {
    "isbjörn" : {"område" : "polar", "art" : "björn", "namn" : "Sven", "happiness" : 90, "ålder" : 22},
    "varg" : {"område" : "tempererad zon", "art" : "hunddjur", "namn" : "Milo", "happiness" : 40, "ålder" : 6},
    "lejon" : {"område" : "savann", "art" : "stort kattdjur", "namn" : "Kurt", "happiness" : 60, "ålder" : 12},
    "apa" : {"område" : "savann", "art" : "apa", "namn" : "Bengt", "happiness" : 80, "ålder" : 20},
    "elefant" : {"område" : "tropisk", "art" : "elefanter", "namn" : "Mohammed", "happiness" : 75, "ålder" : 10},
    "gorilla" : {"område" : "tropisk", "art" : "östlig gorilla", "namn" : "Mahmud", "happiness" : 50, "ålder" : 25},
    "sköldpadda" : {"område" : "subtropisk", "art" : "sköldpaddor", "namn" : "Armor", "happiness" : 100, "ålder" : 50},
    "ödla" : {"område" : "subtropisk", "art" : "fjällbärande kräldjur", "namn" : "Gecko", "happiness" : 95, "ålder" : 2}
}

while True: 

    Animal_Place = []

    for animal, info in zoo.items():
        area = info["område"]
        if area not in Animal_Place:
            Animal_Place.append(area)

    print("Välkommen till zoo zoo")
    print("Detta är dina alternativ:")
    print("1. Visa område")
    print("2. Lägga till djur")
    print("3. Hälsa på djuren")
    print("4. Visa rapport")

    choice = int(input("Vad vill du göra: "))

    if choice == 1:
       for area in Animal_Place:
           print("-", area)    
       What_area = input("Ange platsen du vill gå till: ")
       if What_area not in Animal_Place: 
            print("Den zonen finns inte.")
            input("Tryck enter för att köra igen.")
            continue
       for item, zoo_items in zoo.items():
            if zoo_items["område"] == What_area:
                print("-", item)
    elif choice == 2: 
       Animal_add = input("Skriv djuret som ska läggas till: ")
       Animal_area = input("Ange zonen som djuret bor i: ")
       Animal_race = input("Ange djurarten: ")
       Animal_name = input("Ange namnet på detta djur: ")
       if Animal_name and Animal_add in zoo:
           print("Okej...")
       Animal_happiness = int(input("Ange hur glad detta djur är att komma hit: "))
       Animal_age = int(input("Ange djurets ålder: "))
       zoo[Animal_add] = {"område" : Animal_area, "art" : Animal_race, "namn" : Animal_name, "happiness" : Animal_happiness, "ålder" : Animal_age}
    elif choice == 3:
        see_list = input("Vill du se listan på områden? ")
        if see_list == 'ja':
            for area in Animal_Place:
                print("-", area)
        else:
            print("-", "Okej, ingen lista.")
        visit_animals = input("Vilken av platserna vill du besöka? ")
        if visit_animals in Animal_Place:
            print(f"Du går till {visit_animals}, vänta lite.")
            time.sleep(1), print("."), time.sleep(1), print("."), time.sleep(1), print("."), time.sleep(1)
            print("Okej, du är nu framför en skylt som ger dig 3 alternativ."), time.sleep(2)
            print("1. Mata"), time.sleep(1)
            print("2. Leka"), time.sleep(1)
            print("3. Städa"), time.sleep(1)
            Chosen_to_do = int(input("Vad vill du göra: "))
            if Chosen_to_do == 1:
               print("Du matar djuren.")
               for animals, info in zoo.items():
                    if info["område"] == visit_animals:
                        info["happiness"] += 5
                        print(f"{animals} blev gladare tack vare att du matade dem! Happiness: {info["happiness"]}")                
            elif Chosen_to_do == 2:
               print("Du leker med djuren.")
               for animals, info in zoo.items():
                   if info["område"] == visit_animals:
                       info["happiness"] += 10
                       print(f"{animals} blev gladare tack vare att du lekte med dem! Happiness: {info["happiness"]}")
            elif Chosen_to_do == 3:
               print("Du städar djurens område.")
               for animals, info in zoo.items():
                   if info["område"] == visit_animals:
                       info["happiness"] -= 5
                       if info["happiness"] <= 0:
                           print(f"{animals} Happiness nådde 0. Ni är värsta fiender") #osäker om detta printar alla djur eller inte
                           info["happiness"] == 0 
                       else: 
                            print(f"{animals} blev ledsen eftersom du ignorerade dem för att städa... Happiness: {info["happiness"]}")
            else:
                print("Det där var inte ett alternativ.")
                time.sleep(2)
        else:
           print("Denna plats finns inte.")
    elif choice == 4:
        print(f"- Antal djur i detta zoo: {len(zoo)}")
        Happiness = 0
        for djur, info in zoo.items():
            if info["happiness"] > Happiness:
                Happiness = info["happiness"]
        print(f"- Gladaste djuret har {Happiness}% happiness.")
        Oldest = 0
        for djur, info in zoo.items():
            if info["ålder"] > Oldest:
                Oldest = info["ålder"]
        print(f"- Äldsta djuret är {Oldest} år.")
    else: 
        print("Bror.")
    input("Tryck enter för att köra igen.")