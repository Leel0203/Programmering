

class Vehicle:

    def __init__(self, brand : str, model : str, year : int, color : str, milage : float, value : float):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.milage = milage
        self.value = value

    def __str__(self):
        return f"{self.brand}:" + f"(Model: {self.model}) (Year: {self.year}) (Color: {self.color}) (Milage: {self.milage}) (Value: {self.value})"
    
    #def drive(self, distance):  #öka milage baserad på distans
    #self.milage += distance
    #return self.milage
    
    class Car:
        def __init__(self, ac_on):
            self.ac_on = bool

        def toggle_ac():    #gör vadå?
            pass

    class Motorbike:
        def __init__(self, bike_type):
            self.bike_type = bike_type

        def toggle_riding_self():   #kunna välja mellan normal, eco, sport när man kör
            pass

    class Truck:
        def __init__(self, load : int, max_load : int):
            self.load = load
            self.max_load = max_load
        
        def add_load(self, weight):
            if self.load + weight < self.max_load:
                self.load += weight
            else:
                print("\n\nWeight surpasses max load.")
            

def show_cars():
    print("\n" * 20)
    for i, car in enumerate(cars):
        print("-", i + 1, car)

cars = [
    Vehicle("volvo", "sedan", 1444, "blue", 2000, 35000),
    Vehicle("volkswagen", "id.4", 1900, "piss yellow", 1000, 480000), 
    Vehicle("toyota", "corolla", 1800, "green", 5000, 230000)
]

print("\n" * 20 + "1. Show cars\n2. Add Vehicle\n3. Sell vehicleq. quit")
choice = input("What would you like to do?\nYou: ")

if choice == "1": #show cars
    show_cars()
    input("\nPress enter to continue...")
elif choice == "2": #add cars
    pass
elif choice == "3": #sell cars
    
    while True:
        try:
            car_choice = int(input("Enter the number corresponding to the car you want to drive: ")) - 1
            break
        except ValueError:
            print("Try again")