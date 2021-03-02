from kivy.uix.screenmanager import Screen # Pokud chci, aby využíval vždy obrazovku
from kivymd.app import MDApp # Knihovna kivymd
from kivymd.uix.button import MDRectangleFlatButton # Připravené komponenty ke knihovně md - zde tlačítko


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(
                text="Hello, World",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
        )
        return screen


MainApp().run()