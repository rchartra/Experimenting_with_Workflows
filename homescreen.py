from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.label = Label(text="Hello World")
        self.add_widget(self.label)
        self.note = "I am a note"