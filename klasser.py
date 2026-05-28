class Character:
    name: str
    hp : int
    damage : int

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = 10

    def __str__(self):
        return self.name

    def attack_enemy(self, enemy):  #very good function if very good meant very bad
        enemy.hp -= self.damage
        self.hp -= enemy.damage
        print("\n" * 20 + f"{enemy} took {self.damage} points of damage\n{self.name} took {enemy.damage} points of damage")
        input("Press enter to continue...")
    
    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
            print("\nHealth is rounded to the maximum number (100)")
            input("Press enter to continue")

    def is_alive(self): #works for all
        return self.hp > 0

person = Character(input("What is your name?\nYou: "))
enemy = Character(input("Who are you fighting against?\nYou: "))

while True:
    choice = input("\n" * 20 + "1. Attack enemy\n2. Heal\nYou: ").lower()

    if choice == "1":
        person.attack_enemy(enemy)
    elif choice == "2":
        try:
            person.heal(int(input("\n" * 20 + "How much are you healing?\nYou: ")))
        except ValueError:
            print("\n" * 20 + "Very funny")
            input("Press enter to continue...")
            continue
    else:
        print("\n" * 20 + "Input either 1 or 2")
        input("Press enter to continue...")

    if not enemy.is_alive():
        print("\n" * 20 + f"You have defeated {enemy.name}!")
        break

    if not person.is_alive():
        print("\n" * 20 + f"You somehow died to {enemy.name} (skill issue)")
        break

    #osäker på om det var såhär du ville att uppgiften skulle göras, men den funkar någorlunda