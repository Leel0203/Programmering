from nicegui import ui

ui.add_css('''
.line_through {
    text-decoration: line-through;
}
''')

def add_task():
    if task_input.value: #makes sure its not empty
        with task_list:
            with ui.list() as item:
                with ui.row():
                    task_label = ui.label(task_input.value).style("font-size: 200%")
                    ui.button('done', on_click=lambda: toggle_done(task_label))
                    ui.button('remove', on_click=lambda: remove_task(item))
        task_input.value = ""

def remove_task(item):
    item.delete()

def toggle_done(label):
    label.classes(toggle='line_through')

ui.label("To Do List📋")

task_input = ui.input(label='write a list', placeholder='start typing',
         validation={'Input too long': lambda value: len(value) < 20})

ui.button('add', on_click=lambda: add_task())

task_list = ui.list().props('dense separator')

ui.run(native=True)