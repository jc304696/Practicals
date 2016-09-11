"""
    Name: Lyle Martin
    Do it your self exercise Lab 6
    create a GUI using kivy to convert miles to kilometres.

"""

from kivy.app import App
from kivy.lang import Builder

class ConvertDistanceApp(App):
    """Convert miles to kilometres GUI"""
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('distance_converter.kv')
        return self.root

    def handle_conversion(self):
        print('test')
        try:
            kilometres = int(self.root.ids.input.text) * 1.6
        except ValueError:
            kilometres = 0
        self.root.ids.display.text = str(kilometres) + ' Km'

    def handle_increment(self, increment):
        number = int(self.root.ids.input.text) + increment
        self.root.ids.input.text = str(number)
        self.handle_conversion()

ConvertDistanceApp().run()