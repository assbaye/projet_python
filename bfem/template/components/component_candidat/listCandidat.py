import sys
import os

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

class ListeCandidats(Screen):
    candidats = ListProperty([])

    def on_kv_post(self, base_widget):
        self.load_candidats()
        self.afficher_candidats()
# Appeler l'affichage ici

    def load_candidats(self):
        conn = bdd.connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT prenom, nom, sexe, lieu_naissance, etablissement, epr_facultative
            FROM candidats
        """)
        self.candidats = cur.fetchall()

        conn.close()
    
    def modifier_candidat(self, candidat):
        # Récupérer l'écran du formulaire
        add_candidat_screen = self.manager.get_screen("AddCandidat")
        # Remplir le formulaire avec les données du candidat à modifier
        add_candidat_screen.remplir_formulaire(candidat)
        # Naviguer vers l'écran du formulaire
        self.manager.current = "AddCandidat"


    def afficher_candidats(self):
        self.ids.candidat_list.clear_widgets()

        for candidat in self.candidats:
            prenom, nom, sexe,lieu_naissance, etablissement, epr_facultative = candidat

            card = MDCard(orientation="vertical", size_hint=(0.45, None), size=("350dp", "200dp"),
                          padding="10dp", spacing="10dp", radius=[20, 20, 20, 20],
                          md_bg_color=[0.9, 0.95, 1, 1])  # Bleu très clair

            box = MDBoxLayout(orientation="vertical", spacing="5dp")

            box.add_widget(MDLabel(text=f"{prenom} {nom}", font_style="H6", bold=True))
            box.add_widget(MDLabel(text=f"{sexe} | {lieu_naissance}", font_style="Caption", theme_text_color="Secondary"))
            box.add_widget(MDLabel(text=f"{etablissement} | {epr_facultative}", font_style="Caption", theme_text_color="Secondary"))
            

            action_box = MDBoxLayout(orientation="horizontal", spacing="10dp")

            btn_modifier = MDRaisedButton(text="Modifier", md_bg_color=[0.2, 0.6, 1, 1])
            
            btn_modifier.bind(on_release=lambda btn, c=candidat: self.modifier_candidat(c))
            btn_details = MDRaisedButton(text="Détails", md_bg_color=[0.2, 0.6, 1, 1])

            action_box.add_widget(btn_modifier)
            action_box.add_widget(btn_details)

            card.add_widget(box)
            card.add_widget(action_box)

            self.ids.candidat_list.add_widget(card)

class AddCandidat(Screen): #ajouter cette classe
    pass

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def on_start(self):
        self.root.current_screen.afficher_candidats()

KV = """
ScreenManager:
    ListeCandidats:
    AddCandidat:
        name : "add_candidat"

<ListeCandidats>:
    name: "liste_candidats"

    BoxLayout:
        orientation: 'vertical'
        
        MDBoxLayout:
            spacing: 10
            padding: [20, 10, 20, 10]
            adaptive_height: True
            md_bg_color: [0.8, 0.9, 1, 1]  # Bleu clair

        ScrollView:
            MDGridLayout:
                id: candidat_list
                cols: 2
                spacing: 20
                padding: [20, 10, 20, 10]
                adaptive_height: True
"""

if __name__ == '__main__':
    MainApp().run()