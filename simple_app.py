from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.label = Label(text="Hello World")
        self.add_widget(self.label)

class simple_app(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(HomeScreen(name="HomeScreen"))
        return root

if __name__ == "__main__":
    simple_app().run()