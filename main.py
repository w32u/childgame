import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text='Hello World!')

if __name__ == '__main__':
    MainApp().run()