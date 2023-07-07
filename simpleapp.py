from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.label = Label(text="Hello World", size_hint=(1, 0.5), pos_hint={'top': 1})
        self.add_widget(self.label)
        self.note = "I am a note"
        self.button = Button(text="Push me", size_hint=(1, 0.5))
        self.add_widget(self.button)
        self.button.bind(on_release=lambda x: self.button_press())

    def button_press(self):
        self.label.text = "Button was pressed!"

class SimpleApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(HomeScreen(name="HomeScreen"))
        return root

    def clean_up(self):
        """Closes resources when the app is done.

        Used in testing.
        """
        pass

if __name__ == "__main__":
    SimpleApp().run()