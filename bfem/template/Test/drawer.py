from kivymd.uix.list import MDList
from kivy.uix.filechooser import ScreenManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout



class Drawer(BoxLayout):

    def __init__(self,screen_manager=None,**kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.orientation ="vertical"
        self.padding = "8dp"

        #definition de la liste dans la sidebar
        ## on instancie une liste scrolable 
        self.scroll_view =ScrollView()
        # # on recupere la liste de navigation 
        self.md_list = self.create_navigation_list()
        # on ajoute la liste de navigation au niveau de l'instance de liste scrolable
        self.scroll_view.add_widget(self.md_list)
        # # on ajoute maintenat l'instance scrolable au niveau boxlayout
        self.add_widget(self.scroll_view)
    

    def create_navigation_list(self):
        md_list =MDList()


        # on ajout des element de la liste
        for page in ["Dasboard","Candidat","Matiere","Evaluation"]:
            md_list.add_widget(OneLineListItem(
                text=page,
                on_press= lambda x, page=page: self.change_screen(page)

            )) 
        return md_list
    
    def change_screen(self,page):
        
        self.screen_manager.current = page

        self.screen_manager.parent.set_state("close")
