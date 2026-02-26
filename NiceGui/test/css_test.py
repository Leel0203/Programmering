from nicegui import ui

ui.add_css('''
    @layer utilities    {
        .class1 {
            background-color: green !important;
        }
    }   
''')

ui.button("Colored Button").classes('class1')
