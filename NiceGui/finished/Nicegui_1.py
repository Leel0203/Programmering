from nicegui import ui

def calculate_fahrenheit(celsius):
    if type(celsius) is not float:
        return
    
    celsius = float(celsius)
    fahrenheit = (celsius * 1.8) + 32
    fahrenheit_label.text = f"That is: {fahrenheit}°f"

ui.label("Celsius to Fahrenheit!")
ui.number("Celsius: ", 
         on_change = lambda e: calculate_fahrenheit(e.value))
fahrenheit_label = ui.label("Enter celsius to have it converted to fahrenheit")

ui.run(native=True)