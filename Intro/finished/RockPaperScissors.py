import random

def har_en_tredjedels_chans():
    slumptal = random.randint()

while True:
    print("Rock, paper, scissors")
    print("Answer in small letters")

    x = input("You: ")

    y = random.randint(1, 3)

    while True:
        if y == 1 and x == "rock":
            print("Bot: rock")
            print("Draw!")
            break
        elif y == 1 and x == "paper":
            print("Bot: rock")
            print("You won!")
            break
        elif y == 1 and x == "scissors":
            print("Bot: rock")
            print("You lost!")
            break
        else:
            break
    
    while True:
        if y == 2 and x == "rock":
            print("Bot: paper")
            print("You lost!")
            break
        elif y == 2 and x == "paper":
            print("Bot: paper")
            print("Draw!")
            break
        if y == 2 and x == "scissors":
            print("Bot: paper")
            print("You won!")
            break
        else:
            break
    
    while True:
        if y == 3 and x == "rock":
            print("Bot: scissors")
            print("You won!")
            break
        elif y == 3 and x == "paper":
            print("Bot: scissors")
            print("You lost!")
            break
        elif y == 3 and x == "scissors":
            print("Bot: scissors")
            print("Draw!")
            break
        else: 
            break
    input("Tryck för att köra igen.")   #Koden är inte jätte optimerad, men den duger för nu. Säkert möjligt att få denna kod under 10 rader.
    #Jag gick tillbaka och fixade denna kod btw det är därför den ser ut såhär (tror lowk inte den fungerade innan lol)