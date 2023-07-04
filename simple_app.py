from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from homescreen import HomeScreen

class simple_app(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(HomeScreen(name="HomeScreen"))
        return root

if __name__ == "__main__":
    simple_app().run()