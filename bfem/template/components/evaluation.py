from kivy.uix.accordion import StringProperty
from kivymd.uix.datatables.datatables import MDDropdownMenu
from kivy.uix.accordion import Widget
from kivy.uix.effectwidget import Rectangle
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.behaviors.toggle_behavior import MDRectangleFlatIconButton
from kivy.uix.filechooser import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from .component_evaluation.Anonymat import Anonymat
from .component_evaluation.Note import Note
from .component_evaluation.Deliberation import ListDeliberation

from kivymd.app import MDApp

KV = """
<Evaluation> :
    MDNavigationLayout:

        MDScreenManager:
            id:"screen_manager"
            MDScreen:
                MDBoxLayout:
                    orientation:"vertical"
                    padding: ('10dp', '10dp', '10dp', '10dp')
                    # md_bg_color:"#000000"
                    

                       
                    
                    MDBoxLayout:
                        id: navigation
                        orientation:"horizontal"
                        # adaptive_width:True
                        size_hint: None, None
                        pos_hint: {'top': 1,}
                        # md_bg_color:"#ffffff"
                        spacing: '10dp'
                        padding: ('10dp', '10dp', '10dp', '10dp')
           
                        MDTextField:
                            id: session
                            hint_text: "Session 1"
                            size_hint: None, None
                            mode:"rectangle"
                            font_size:20
                            height: 30
                            width:300
                            on_focus:if self.focus: root.show_dropdown(self)
                        Widget:
                            size_hint:None, 1


                        
                    ScreenManager:
                        id:screen_manager_current
                        Anonymat:
                            id:anonymat
                        Note:
                            id:note
                        ListDeliberation:
                            id:listdeliveration
                        
                        
                
"""

Builder.load_string(KV)
class Evaluation(MDScreen):
    session = StringProperty("Session 1")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = 20
        self.radius = 20

    def setsession(self,matiere):
        self.session = matiere

    def on_kv_post(self, base_widget):
        self.addnavigation()

    def switch_navigation(self,instance,screen_manager_content=None):
       
        """
        On l'appel si on veut changer d'ecran
        """
        screen_name = instance.text  # Utilisation du texte du bouton pour identifier l'écran
        # screen_manager_content.current = screen_name

        for nav in self.list_navigation:
            if nav["text"] == screen_name:
                screen_manager_content.current = nav["screen"].name
                return
    def addnavigation(self):

           # Accéder à l'ID 'navigation' du fichier KV
        box_layout = self.ids.navigation
        current_screen = self.ids.screen_manager_current

        # Liste des éléments de navigation
        self.list_navigation = [
            {
                "text": "Anonymat",
                "icon": "book-plus",
                "screen": Anonymat(name="Ananymous")
            },
             {
                "text": "Note",
                "icon": "book-plus",
                "screen": Note(name="Note")
            },
            {
                "text": "Deliberation",
                "icon": "book-plus",
                "screen": ListDeliberation(name="deliberation")
            },
           
        
           
           
        ]

        # Ajouter chaque écran dans le ScreenManager
        for nav in self.list_navigation:
            current_screen.add_widget(nav["screen"])

        # Créer les boutons pour chaque élément de navigation
        for nav in self.list_navigation:
            bouton_navigation = MDRectangleFlatIconButton(
                icon=nav["icon"],
                text=nav["text"],
                on_press=lambda instance, screen_manager_content=current_screen: self.switch_navigation(instance, screen_manager_content)
            )
            box_layout.add_widget(bouton_navigation)
    
    def open_menu(self,text_field):
      
        #  interface_matiere = Matiere()
        menu_items = [
            {"text":"Session 1", "viewclass": "OneLineListItem", 
             "on_release": lambda x="Session 1": self.select_matiere(x)},

             {"text":"Session 2", "viewclass": "OneLineListItem", 
             "on_release": lambda x="Session 2": self.select_matiere(x)}
           
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.session,
            items=menu_items,
            width_mult=4
        )
        self.menu.open()

    def select_matiere(self, session):
        self.ids.session.text = session
        self.ids.listdeliveration.set_session(session)
        self.ids.anonymat.set_session(session)
        self.ids.note.set_session(session)
        self.menu.dismiss()
       
 
    def show_dropdown(self, textfield):
        """Affiche le menu déroulant sous le champ MDTextField."""
        # matiere = Matiere()
        if not textfield:  # Vérification si textfield est valide
            print("Erreur: textfield est None")
            return
        
        menu_items = [
              {"text":"Session 1", "viewclass": "OneLineListItem", 
             "on_release": lambda x="Session 1": self.select_matiere(x)},

             {"text":"Session 2", "viewclass": "OneLineListItem", 
             "on_release": lambda x="Session 2": self.select_matiere(x)}
        ]
        
        self.menu = MDDropdownMenu(
            caller=textfield,
            items=menu_items,
            width_mult=4,
        )

        if self.menu:
            self.menu.open()

    # def set_matiere(self, textfield, value):
    #     print(value)
    #     textfield.text = value
        
    #     self.ids.note.setsession(value)
    #     # self.set_matiere(value)
    #     if self.menu:
    #         self.menu.dismiss()


# 
# class Example(MDApp):

#     def build(self):
#         return Evaluation()

# Example().run()