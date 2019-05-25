# Backbone of the application.
import kivy
kivy.require('1.10.1')

# Required modules of the "kivy"-framework.
from kivy.app import App
from kivy.uix.label import Label

# Class representing the application. Everything that happens in the application is controlled from here.
class TextAdventure(App):

    # Builds the graphical user interface of the application.
    def build(self):
        return Label(text='Hello world')

# Runs the application.
TextAdventure().run()