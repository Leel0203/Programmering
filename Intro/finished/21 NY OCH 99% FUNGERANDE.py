last_picked_1 = None
last_picked_2 = None

print("Välj ett nummer 1 - 2")
print("spelaren som når 21 vinner")
print("Går man över 21 så vinner motståndaren")
print("Man får inte köra samma nummer 3 gånger på rad.")    #lite mer komplicerad att implementera än jag trodde

number_21 = 0

while True:
    while True:
        try:    #stal try + except ValueError B)
            player_1_number = int(input("Spelare 1: "))
        except ValueError:  
            print("Sluta trolla Brochacho.")
            continue
        number_21 += player_1_number
        if player_1_number <= 0:
            print("Bror va göru.")
            number_21 -= player_1_number
            continue
        elif player_1_number >= 3:
            print("1 eller 2 bror.")
            number_21 -= player_1_number
            continue
        break

    if number_21 == 21:
        print("Spelare 1 vann!")
        break
    elif number_21 >= 21: 
        print("Spelare 2 vann!")
        break
    print(f"21 : {number_21}")

    while True:
        try:    #stal try + except ValueError B)
            player_2_number = int(input("Spelare 2: "))
        except ValueError:
            print("Sluta trolla Brochacho.")
            continue
        number_21 += player_2_number
        if player_2_number <= 0:
            print("Bror va göru.")
            number_21 -= player_2_number
            continue
        elif player_2_number >= 3:
            print("1 eller 2 bror.")
            number_21 -= player_2_number
            continue
        break

    if number_21 == 21:
        print("Spelare 2 vann!")
        break
    elif number_21 >= 21:
        print("Spelare 1 vann!")
        break
    print(f"21 : {number_21}")