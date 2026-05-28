import time

class Car:
    def __init__(self, brand : str, model : str, year : int, color : str, milage : float, value : float):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.milage = milage   #mil
        self.value = value

    def __str__(self):
       return f"{self.brand}:" + f"(Model: {self.model}) (Year: {self.year}) (Color: {self.color}) (Milage: {self.milage}) (Value: {self.value})"

    def drive(self, distance):  #öka milage baserad på distans
        self.milage += distance
        return self.milage
    
def car_list(): #används inte just nu, men hade sparat plats
    see_list = input("Do you wish to see the list of cars?\nYou: ").lower()
    if see_list == "yes":
        print("\n" * 20)
        for car in sorted(cars, key=lambda car: car.brand):   #sorterar baserat på brandet
            print("-", car)
    else:
        input("\n" * 20 + "\nList of cars was skipped\n\nPress enter to continue...")
              
cars = [
    Car("volvo", "sedan", 1444, "blue", 2000, 35000), 
    Car("volkswagen", "id.4", 1900, "piss yellow", 1000, 480000), 
    Car("toyota", "corolla", 1800, "green", 5000, 230000)
]

bank_account = 0

while True:
    choice = input("\n" * 20 + "1. Show cars\n2. Add car\n3. Sell car\n4. Drive car\n5. Newest car\n\nYou: ")

    if choice == "1":   #gör så man kan söka efter ett märke
        print("\n" * 20)
        for car in sorted(cars, key=lambda car: car.brand):   #sorterar baserat på brandet
            print("-", car)
        input("\nPress enter to continue...")
    elif choice == "2": #Mata in information för ny bil
        car_type = input("\n" * 20 + "Enter the car type (ex: volvo): ")
        model = input("Enter the cars model: ")
        color = input("Enter the cars color: ")
        while True:
            try: 
                year = int(input("Enter the cars manufacture year: "))
                milage = int(input("Enter how many mil the car has driven (sv mil): "))
                value = float(input("Enter the cars value (kr): "))
                break
            except ValueError:
                print("\nEnter valid integers for year and milage")
                input("Press enter to continue")
        cars.append(Car(car_type, model, year, color, milage, value))
    elif choice == "3": #Säljer bil, måste sänka värdet på bilen beroende på om den körts och dess milage
        while True:
            print("\n" * 20)
            for car in sorted(cars, key=lambda car: car.brand):   #sorterar baserat på brandet
                print("-", car)
            sell_car = input("\nWhat brand of car do you wish to sell?\nYou: ")
            sell_car_model = input("What model is that?\nYou: ")
            found_car = None
            for car in cars:
                if car.brand == sell_car and car.model == sell_car_model:
                    found_car = car
                    break

            if found_car == None:
                print("Enter a correct car and model")
                input("Press enter to continue...")
                continue

            sell_choice = input(f"\nAre you sure you want to sell this {sell_car} {sell_car_model}?\nYou: ")
            if sell_choice != "yes":
                continue

            milage_sell = found_car.milage  #kan ha ett standardvärde på bilen och sedan sänka det beroende på milagen 
            bank_account += found_car.value
            print("\n" * 20 + f"With the car sold your current bank account is: {bank_account}")
            input("\nPress enter to continue...")
            
            cars.remove(found_car)
            restart = input("\n" * 20 + "Do you wish to sell another car?\nYou: ").lower()
            if restart != "yes":
                break
    elif choice == "4": # köra bil
        print("\n" * 20)
        for i, car in enumerate(cars):
            print("-", i + 1, car)
        while True:
            try:
                car_choice = int(input("Enter the number corresponding to the car you want to drive: ")) - 1
                break
            except ValueError:
                print("Try again")

        distance = float(input("\nHow far are you driving (mil): "))
        cars[car_choice].drive(distance)
        print(f"{car_choice} now has a total of {distance}")
    elif choice == "5": #printa ut information om bilen med nyast årsmodell (year)
        for car in sorted(cars, key=lambda car: car.year):
            print("-", car)
    else:
        print("Enter a number from 1 - 3 brotato")