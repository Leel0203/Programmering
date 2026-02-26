from nicegui import ui

@ui.page("/")
def home_page():
    ui.label("Answer all questions")
    ui.label("The correct answer will be displayed after answering each question")
    ui.link("Question 1", "/question 1")
    ui.link("Question 2", "/question 2")
    ui.link("Question 3", "/question 3")
    ui.link("Question 4", "/question 4")

@ui.page("/question 1")
def question_1():
    ui.label("Question 1")
    ui.label("How much does the sun approximately weigh?")
    ui.button("1.62 x 10^29", on_click=lambda: answer("incorrect"))
    ui.button("1.98 x 10^30", on_click=lambda: answer("correct"))
    ui.button("2.21 x 10^31", on_click=lambda: answer("incorrect"))

    ui.link("homepage", "/")

@ui.page("/question 2")
def question_2():
    ui.label("Question 2")
    ui.label("What did I eat yesterday?")   #and "the most creative person of the year" award goes tooooooooo Leo

    ui.button("Burger", on_click=lambda: answer("correct"))
    ui.button("Pizza", on_click=lambda: answer("incorrect"))
    ui.button("Taco", on_click=lambda: answer("incorrect"))

    ui.link("homepage", "/")

@ui.page("/question 3")
def question_3():
    ui.label("Question 3")
    ui.label("How many hours of sleep did I get last night?")

    ui.button("10", on_click=lambda: answer("incorrect"))
    ui.button("4", on_click=lambda: answer("incorrect"))
    ui.button("3", on_click=lambda: answer("correct"))

    ui.link("homepage", "/")

@ui.page("/question 4")
def question_4():
    ui.label("Question 4")
    ui.label("How many tires does a car have?")
    ui.label("Answer in either words or numbers.")

    def submit():
        if text.value == "four" or text.value == "4":
            answer("correct")
        else:
            answer("incorrect")           

    text = ui.input(label='Type something')
    text.on('keydown.enter', submit)

    ui.link("homepage", "/")

def answer(choice):
    ui.notify(f"You were {choice}") #första gången ja någonsin sparat utrymme

ui.run()    #lowk rolig uppgift