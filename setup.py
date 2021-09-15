import kivy
from kivy.app import App
from kivy.uix.button import Button

#kivy.require("1.10.1")

class TestApp(App):
    def build(self):
        return Button(text="Hello World")


TestApp().run()
