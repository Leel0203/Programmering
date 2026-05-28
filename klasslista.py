

while True:
    students = {}

    try:
        choice = int(input(
            "1. Lägga till en elev \n" \
            "2. Visa alla elever \n" \
            "3. Visa elever per läsår \n" \
            "4. Quit \n" \
            "Choice: "
            ))
    except ValueError:
        print("Ange en siffra 1 - 4")
        input("\nTryck enter för att fortsätta")
        continue

    if choice == 1:
        with open("students.txt", "a", encoding="utf-8") as file:
            name = input("Ange elevens namn: ")    #lägga till så man inte kan ange en int
            try:
                year = int(input("Ange elevens läsår: "))
            except ValueError:
                print("Ange korrekt läsår")
                continue
            file.write(f'{name} ({year})\n')    #kan köra file.write("\n".join(students)), but if it aint broke dont fix it
    
    with open("students.txt", "r", encoding="utf-8") as file:
        for lines in file.read().split("\n"):
            if not lines:   #osäker varför detta behövs
                continue

            name, year = lines.split(" (")  #hela den här delen blankar för mig, men hittade inget annat
            year = int(year[:-1])

            if year not in students:
                students[year] = []
            
            students[year].append(name)

    if choice == 2:
        for names in students.values():
            for name in names:
                print("-", name)
        input("\nTryck enter för att fortsätta")
    elif choice == 3:   #visa elever per läsår
        for year in sorted(students):
            print(f'År {year}: {', '. join(students[year])}')   #one liner yes, men vi lärde oss precis join
        input("\nTryck enter för att fortsätta")
    elif choice == 4:
        print("Bye bye")   
        break
    elif choice < 1 or choice > 4:
        print("1 - 4")
        input("\nTryck enter för att fortsätta")
        continue

    #må försöka flytta på klasslista.py och students.txt så de inte bara sitter utanför allt. (alltså så de istället är i t ex finished)