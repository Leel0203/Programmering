from nicegui import ui
import random

def player_2_sort_of_ai():
    return random.randint(1, 3)

def ai_options(choice_2):
    if choice_2 == 1:
        choice_2_show.text = f"Ai picked rock"
    elif choice_2 == 2:
        choice_2_show.text = f"Ai picked paper"
    elif choice_2 == 3:
        choice_2_show.text = f"Ai picked scissors"

def options(choice):
    choice = choice.strip().lower()
    if choice not in ("rock", "paper", "scissors"):
        choice_show.text = "Type rock, paper or scissors only."
        return
    
    choice_show.text = f"You picked {choice}"

    ai_pick = player_2_sort_of_ai()
    ai_options(ai_pick)
    
ui.label("Rock Paper Scissors!")

input_box = ui.input("You: ")
input_box.on("Hej", lambda e: options(e.value))  #on_submit ville verkligen inte fungera
             
choice_show = ui.label("...")

ui.label("Ai: ")
choice_2_show = ui.label("...")

ui.run(native=True)