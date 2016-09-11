"""name: Lyle Martin

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class CreateWidgetApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Lyle', 'David', 'Martin']

    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Button(text=name)
            self.root.ids.boxes.add_widget(temp_button)

CreateWidgetApp().run()