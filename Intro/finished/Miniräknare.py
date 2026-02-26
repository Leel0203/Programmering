def addition(x, y):
        return x + y
def subtraction(x, y):
        return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if x==0 and y==0:
        print("Kan inte dela med noll") #fungerar inte
        return "FEL"
    return x / y
def power_of(x, y):
        return x ** y
        
while True:
      
    print("Nummer 1:")
    number_1 = int(input())

    print("Nummer 2:")
    number_2 = int(input())

    print("Vill du addera (+), subtrahera (-), multiplicera (*), dividera (/) eller upphöjt i (**) ?")
    print("Skriv i symboler inte bokstäver")

    Val = input()
    if Val == "+":
      result = addition(number_1, number_2)
      print("Ditt nummer är", result)
    elif Val == "-":
      result = subtraction(number_1, number_2)
      print("Ditt nummer är", result)
    elif Val == "*":
        result = multiplication(number_1, number_2)
        print("Ditt nummer är", result)
    elif Val == "/":
        result = division(number_1, number_2)
        if result == "FEL":
            continue
        print("Ditt nummer är", result)
    elif Val == "**":
      result = power_of(number_1, number_2)
      print("Ditt nummer är", result)
    else:
         print("Stor första bokstav och resten liten eller bara små bokstäver")

    print("Vill du köra om miniräknaren?")
    restart = input()

    if restart != "Ja" and restart != "ja":
      print("Okej, hej då")
      break