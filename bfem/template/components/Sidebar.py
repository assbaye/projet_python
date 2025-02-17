from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.uix.boxlayout import BoxLayout

class Sidebar(MDNavigationDrawer):


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.box = BoxLayout(orientation='vertical')
        
        self.list = MDList()

        self.list.add_widget(OneLineIconListItem(text='Accueil', on_release=lambda x: self.switch_screen('main')))
        self.list.add_widget(OneLineIconListItem(text='Paramètres', on_release=lambda x: self.switch_screen('settings')))

        self.box.add_widget(self.list)
        self.add_widget(self.box)

    def switch_screen(self, screen_name):
        self.parent.parent.current = screen_name
