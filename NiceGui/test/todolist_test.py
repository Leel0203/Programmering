from nicegui import ui

ui.add_css('''
    @layer utilities    {
        .class1 {
            background-color: green !important;
        }
        .class2 {
            background-color: blue !important;
        }
    }   
''')

def add_task():
    text = task_input.value
    to_do_list.append(text)

    ui.label(text + "\n")

def remove_task():
    text_2 = task_input_2.value
    to_do_list.pop(text_2)

    

to_do_list = []

task_input = ui.input(label='', placeholder='start typing',
         validation={'Input too long': lambda value: len(value) < 20})

ui.button('add', on_click=lambda: add_task()).classes("class1")

task_input_2 = ui.input(label='', placeholder='start typing',
         validation={'Input too long': lambda value: len(value) < 20})

ui.button('remove', on_click=lambda: add_task()).classes("class2")

ui.run()