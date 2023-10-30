from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.app import Builder
from kivy.uix.boxlayout import BoxLayout

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class Simulacoes(Screen):
    pass

class Opcoes(Screen):
    pass


class Interface(App):
    def build(self):
        return Gerenciador()


Interface().run()