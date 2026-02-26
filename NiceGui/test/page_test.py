from nicegui import ui

@ui.page('/')
def main_page():
    ui.label('Welcome to the main page!')
    ui.link('Go to the other page', '/other_page') #

@ui.page('/other_page')
def other_page():
    ui.label('This is the other page.')
    ui.link('Go to main page', '/')

ui.run()