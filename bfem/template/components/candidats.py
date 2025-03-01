from kivy.uix.accordion import BooleanProperty
from kivymd.uix.behaviors.toggle_behavior import MDRectangleFlatIconButton
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
# from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from .component_candidat.AddCandidat import AddCandidat
from .component_candidat.ListCandidat import ListeCandidats

KV = """
<Candidat> :
    id:base_candidat
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
                        pos_hint: {'center_x': 0.1,'center_y':0.5}
                        # md_bg_color:"#ffffff"
                        spacing: '10dp'
                        padding: ('10dp', '10dp', '10dp', '10dp')
                       
                    ScreenManager:
                        id:screen_manager_current
                        ListeCandidats:
                            id:listeCandidat
                        AddCandidat:
                            id:addcandidat
                        
                
"""
Builder.load_string(KV)

class Candidat(MDScreen):
    statdata = BooleanProperty(True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 20
        self.radius = 20

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
                if nav["screen"].name == " ListeCandidat":
                    self.ids.listeCandidat.load_ListeCandidat()
                return
    def addnavigation(self):
           # Accéder à l'ID 'navigation' du fichier KV
        box_layout = self.ids.navigation
        current_screen = self.ids.screen_manager_current

        # Liste des éléments de navigation
        self.list_navigation = [
             {
                "text": "Liste des candidats",
                "icon": "book-plus",
                "screen": ListeCandidats(name="ListeCandidat")
            },
           
            {
                "text": "Ajouter un candidat",
                "icon": "book-plus",
                "screen": AddCandidat(name="addCandidat")
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

