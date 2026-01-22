while True:
    start = int(input("Nummer 1: "))
    stop = int(input("Nummer 2: "))

    for i in range (start, stop + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)   
    end_program = (input("Vill du köra igen? Y / N")) 
    if end_program != "Y" and end_program != "y":
        print("Hejdå")
        break