from nicegui import ui
import random

ui.add_head_html("""    
<style>
body {
    margin: 0;
}
</style>
""")    #för att fixa kanterna så när man trycker på random background tar den upp hela skärmen. Osäker på dess värde nu när ja använder javascript

value = 0       #current red button value
value_gain = 1  #red button gain

def random_background():
    random_number = random.randint(0, 255)
    if random_number <=250:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        ui.run_javascript(  #okej, lite overkill, men det irriterade mig så in i helvete att bakgrundsfärgen inte tog upp hela skärmen
            f'document.body.style.backgroundColor = "rgb({r},{g},{b})";')
        ui.run_javascript('document.body.style.backgroundImage = "none";')
    else:
        ui.run_javascript(
           f'document.body.style.backgroundImage = \'url("https://i.pinimg.com/736x/bc/74/c4/bc74c421253d97d950406a5b7ecb9692.jpg")\';'
        ) 
        ui.run_javascript('''
            document.body.style.backgroundSize = "cover";
            document.body.style.backgroundRepeat = "no-repeat";
            document.body.style.backgroundPosition = "center";
        ''')    #tänker inte äns försöka förklara mig ur dem här 12 raderna :skull:. idéen var min iaf
def clicked(amount: int):
    global value
    value += amount
    value_label.set_text(str(value))

def gains(cost: int, boost: int):   #väldigt intressant och roligt sätt att använda defs ngl
    global value, value_gain
    if value >= cost:
        value -= cost
        value_gain += boost
        value_label.set_text(str(value))
        gain_label.set_text(str(f"Du får {value_gain} poäng per click"))
    else:
        ui.notify(f"Brorsan hur går det med matten? Du behöver {cost-value} mer poäng för denna.")

def victory(cost: int):
    global value, value_gain
    if value >= cost:
        value -= value
        value_label.set_text(str(value))
        ui.notify("Du vann!🥳🎉")
        value_gain = 1
        gain_label.set_text(str(f"Du får {value_gain} poäng per click"))
    else:
        ui.notify(f"Trodde du deadass att jag skulle missa detta 💀")

with ui.column().classes("relative w-full h-screen items-center justify-center") as main_container:
    with ui.button("", on_click=lambda: clicked(value_gain)).classes('class1').classes("text-4xl w-40 h-40 -mt-40"):
        ui.image("https://i.pinimg.com/736x/a0/26/04/a026043ae078a8bf2b7f117767fd6d16.jpg").classes("absolute inset-0 w-full h-full object-cover")  #må lära mig cssn
        value_label = ui.label(str(value)).classes("text-4xl").classes("absolute inset-0 flex items-center justify-center text-4xl text-red-500 font-bold") #vettefan vad cssn ska mena här ngl
    gain_label = ui.label(str(f"Du får {value_gain} poäng per click"))
    ui.button("10 000 000 pts", on_click=lambda: victory(10000000)) #skulle kunna göra så att när man trycker på denna så ändras bakgrunden till nån annan image

with ui.column().classes("absolute left-0 top-0"):
    ui.button("+1 gain (costs 1 pt)", on_click=lambda: gains(1, 1)).classes("w-30 h-30 absolute left-0 top-0").style("background: #DBDBDB !important; color:blue !important;")
    ui.button("+10 gain (costs 10 pts)", on_click=lambda: gains(10, 10)).classes("w-30 h-30 absolute left-0 top-31").style("background: #B0B0B0 !important; color:blue !important;")
    ui.button("+100 gain (costs 100 pts)", on_click=lambda: gains(100, 100)).classes("w-30 h-30 absolute left-0 top-62").style("background: #919191 !important; color:blue !important;")
    ui.button("+1 000 gain (costs 1 000 pts)", on_click=lambda: gains(1000, 1000)).classes("w-30 h-30 absolute left-0 top-93").style("background: #696969 !important; color:blue !important;")
    ui.button("+10 000 gain (costs 10 000 pts)", on_click=lambda: gains(10000, 10000)).classes("w-30 h-30 absolute left-0 top-124").style("background: #303030 !important; color:blue !important;")
    #balancingen skulle kunna finslipas

ui.button("Random background color 🎲", on_click=lambda: random_background()).classes("fixed bottom-4 right-4")

ui.run(native=True)