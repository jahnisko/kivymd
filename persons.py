import os

from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, TwoLineAvatarListItem, ImageLeftWidget
import json


person_list = [{"name": "Karel Nový", "state": "CZE"},
               {"name": "Ivan Hrozný", "state": "CZE"},
               {"name": "Vítězslav Jahn", "state": "GER"}]


class MyItem(TwoLineAvatarListItem):
    def __init__(self, name, state, hod, image, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = "Jméno osoby"
        self.secondary_text = "Stát osoby"
        self.text = name
        self.secondary_text = state
        self.secondary_text += " , " + hod
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=image)
        self.add_widget(self.image)
        # self pracuji s objekt i s předkem, protože dědím

    def on_press(self):
        print(self.text)

    def on_touch_up(self, touch):
        print(touch)
        self.image.source = "images/green.png"


class Persons(BoxLayout):
    # kwargs a args pro slovníky, listy atd zkrátka arguments
    def __init__(self, *args, **kwargs):
        super(Persons, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        dir_path = os.path.dirname(os.path.realpath(__file__))
        '''for i in person_list:
            list.add_widget(MyItem(name=i['name'], state=i['state']))'''
        with open(dir_path + '/' + 'persons.json', encoding="utf-8") as json_file:
            data = json.load(json_file)
            for i in data["ostepari"]:
                list.add_widget(MyItem(name=i['jmeno'], state=i['narodnost'], hod=i["hod"], image=i['img']))
        scrollview.add_widget(list)
        self.add_widget(scrollview)