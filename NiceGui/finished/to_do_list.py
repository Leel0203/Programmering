from nicegui import ui

def add_task():
    if task_input.value: #makes sure its not empty
        with task_list:
            with ui.list() as item:
                with ui.row():
                    task_label = ui.label(task_input.value).style("font-size: 200%")
                    ui.button(icon="check", on_click=lambda: toggle_done(task_label)).props("color=green")
                    ui.button(icon='delete', on_click=lambda: remove_task(item)).props("color=black")
        task_input.value = ""

def remove_task(item):
    item.delete()

def toggle_done(label):
    label.classes(toggle='text-decoration: line-through')

ui.label("To Do List📋")
#with ui.column().classes("relative w-full h-screen items-center justify-center") as main_container: #vore intressant om ja kunde placera inputen i mitten
with ui.row():
    task_input = ui.input(label='write a list', placeholder='start typing', validation={'Input too long': lambda value: len(value) < 20})
    ui.button('add', on_click=lambda: add_task())

task_list = ui.list().props('dense separator')

ui.run(native=True) #inte det vackraste sättet att göra uppgiften, men den fungerar, typ. 