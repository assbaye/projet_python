from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview.layout import RecycleDataViewBehavior
from kivy.uix.recycleboxlayout import RecycleLayout
from kivy.uix.recycleview import RecycleView
import sys
import os
from kivy.properties import ObjectProperty
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), "../../../.."))
)
from bfem.database.candidat import Candidat
from bfem.database.bdd import bdd

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ListProperty
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window





KV = """
<ListeCandidats>:
    name: "liste_candidats"
    BoxLayout:
        orientation: 'vertical'
        
        MDBoxLayout:
            spacing: 10
            padding: [10, 10, 10, 10]
            adaptive_height: True
            md_bg_color:   "#FF7300"
            MDLabel:
                text: 'La liste des Candidats'
                color: 1 , 1,1,1
                size_hint: 1, None
                halign: "center"
                bold: True
        ScrollView:
            RecycleView:
                id: list
                viewclass: 'CandidatCard'  # La classe utilisée pour afficher chaque élément
                RecycleGridLayout:
                    default_size: 1, dp(200)  # Taille par défaut des éléments
                    default_size_hint: 0.45, None  # Taille horizontale maximale
                    size_hint_y: None  # La hauteur est déterminée par le contenu
                    height: self.minimum_height  # Hauteur minimale pour s'adapter au contenu
                    # orientation: 'vertical'  # Orientation verticale
                    spacing: dp(20)  # Espacement entre les éléments
                    padding: dp(20)  # Marge intérieure
<CandidatCard>:
    orientation: "vertical"
    size_hint: None, None
    size: "350dp", "200dp"
    padding: "10dp"
    spacing: "10dp"
    radius: [20, 20, 20, 20]
    md_bg_color: [0.9, 0.95, 1, 1]

    MDBoxLayout:
        orientation: "vertical"
        spacing: "5dp"

        MDLabel:
            id: label_nom
            font_style: "H6"
            bold: True

        MDLabel:
            id: label_sexe_lieu
            font_style: "Caption"
            theme_text_color: "Secondary"

        MDLabel:
            id: label_etablissement_epreuve
            font_style: "Caption"
            theme_text_color: "Secondary"

    MDBoxLayout:
        orientation: "horizontal"
        spacing: "10dp"

        MDRaisedButton:
            text: "Modifier"
            on_release: root.on_modify()

        MDRaisedButton:
            text: "Détails"
            on_release: root.on_details()
    """
Builder.load_string(KV)

class CandidatCard(RecycleDataViewBehavior, MDCard):
    text = ObjectProperty("")
    secondary_text = ObjectProperty("")
    tertiary_text = ObjectProperty("")
    candidat = ObjectProperty(None)

    def refresh_view_attrs(self, rv, index, data):
        """Actualise la vue avec les nouvelles données."""
        self.text = data["text"]
        self.secondary_text = data["secondary_text"]
        self.tertiary_text = data["tertiary_text"]
        # self.candidat = data["candidat"]
      
        self.ids.label_nom.text = self.text
        self.ids.label_sexe_lieu.text = self.secondary_text
        self.ids.label_etablissement_epreuve.text = self.tertiary_text
        return super().refresh_view_attrs(rv, index, data)

    def on_modify(self):
        print(f"Modification du candidat : {self.candidat}")

    def on_details(self):
        print(f"Détails du candidat : {self.candidat}")

class ListeCandidats(Screen):

    candidats = ListProperty([])

    def __init__(self, **kw):
        super().__init__(**kw)
        
        
    
       

    def on_kv_post(self, *args):
        self.load_candidats()
        self.cols = max(1, int(Window.width / 400))  # Chaque carte fait environ 400px de large
        self.ids.list.children[0].cols = self.cols
        all_candidats = Candidat().get_all_candidate()
        candidats = [
            {
                "text": f"{c[1]} {c[2]}",
                "secondary_text": f"{c[4]} | {c[3]}",
                "tertiary_text": f"{c[5]} | {c[7]}",
                "candidat": c,
            }
            for c in all_candidats
        ]

        print(all_candidats)
        self.ids.list.data = candidats
        
       
# Appeler l'affichage ici

    def load_candidats(self):
        """Charge la liste des candidats depuis la base de données"""
        all_candidats = Candidat().get_all_candidate()
        candidats = [
            {
                "text": f"{candidat[1]} {candidat[2]}",  # Prénom et nom
                "secondary_text": f"{candidat[5]} | {candidat[3]}",  # Sexe et lieu de naissance
                "tertiary_text": f"{candidat[8]} | {candidat[6]}",  # Établissement et épreuve facultative
                "on_release": lambda c=candidat: self.modifier_candidat(c),  # Action lors du clic
            } for candidat in all_candidats
        ]
        # print(all_candidats)
        self.ids.list.data = candidats
    
    def modifier_candidat(self, candidat):
       if candidat:
            add_candidat_screen = self.manager.get_screen("AddCandidat")
            add_candidat_screen.remplir_formulaire(candidat)
            self.manager.current = "AddCandidat"
       else:
            print("Erreur : Aucun candidat sélectionné.")



  

class MainApp(MDApp):
    def build(self):

        return ListeCandidats()

    # def on_start(self):
    #     self.root.current_screen.afficher_candidats()


if __name__ == '__main__':
    print(Candidat().get_all_candidate())
    MainApp().run()
