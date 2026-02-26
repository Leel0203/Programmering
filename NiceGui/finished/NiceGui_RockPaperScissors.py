from nicegui import ui
import random

player_choice_value = ""
ai_choice_value = ""

def ai_random():
    return random.choice(["rock", "paper", "scissors"])

def ai_options(choice_2):
    ai_choice.text = f"AI picked {choice_2}"

def options(choice):
    global player_choice_value, ai_choice_value

    player_choice.text = f"You picked {choice}"
    player_choice_value = choice

    ai_choice_value = ai_random()
    ai_options(ai_choice_value)

    update_results(player_choice_value, ai_choice_value)

def update_results(player_choice, ai_choice):
    if ai_choice == player_choice:
        results.text = "It's a tie."
    elif player_choice == "rock" and ai_choice == "scissors":
        results.text = "You win!"
    elif player_choice == "paper" and ai_choice == "rock":
        results.text = "You win!"
    elif player_choice == "scissors" and ai_choice == "paper":
        results.text = "You win!"
    else:
        results.text = "AI wins!"

ui.label("Rock Paper Scissors!")

player_choice = ui.label("...")
ai_choice = ui.label("...")
results = ui.label("")

with ui.row():
    ui.button("Rock", on_click = lambda _: options("rock"))
    ui.button("Paper", on_click = lambda _: options("paper"))
    ui.button("Scissors", on_click = lambda _: options("scissors"))

ui.run(native=True) #ska inte ljuga denna uppgift var fan svår. Kan cirka 50% av vad som händer här.