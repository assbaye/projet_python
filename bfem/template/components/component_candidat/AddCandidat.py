import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), "../../../.."))
)
from bfem.database.candidat import Candidat
from bfem.database.bdd import bdd
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty

KV = """
ScreenManager:
    AddCandidat:

<AddCandidat>:
    name: "add_candidat"
    sexe: "M"
    epreuve_facultative: "Dessin"
    lv2: "LV2"
    type_candidat: "Officiel"
    
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 20
        padding: [20, 20, 20, 20]
    
        
        ScrollView:
            MDGridLayout:
                cols: 2
                spacing: 15
                adaptive_height: True

                MDTextField:
                    id: prenom
                    hint_text: "Prénom"
                    mode: "rectangle"
                
                MDTextField:
                    id: nom
                    hint_text: "Nom"
                    mode: "rectangle"
                
                MDTextField:
                    id: date_naissance
                    hint_text: "Date de naissance"
                    mode: "rectangle"
                
                MDTextField:
                    id: lieu_naissance
                    hint_text: "Lieu de naissance"
                    mode: "rectangle"
                
                MDTextField:
                    id: nationalite
                    hint_text: "Nationalité"
                    mode: "rectangle"
                
                MDTextField:
                    id: etablissement
                    hint_text: "Etablissement"
                    mode: "rectangle"
                
                MDTextField:
                    id: aptitude_sportive
                    hint_text: "Aptitude Sportive"
                    mode: "rectangle"
                
                MDRaisedButton:
                    id: sexe
                    text: root.sexe
                    on_release: root.open_menu(self, 'sexe')
                
                MDRaisedButton:
                    id: epreuve_facultative
                    text: root.epreuve_facultative
                    on_release: root.open_menu(self, 'epreuve_facultative')

                MDTextField:
                    id: moyenne_6e
                    hint_text: "Moyenne 6e"
                    mode: "rectangle"
                
                MDTextField:
                    id: moyenne_5e
                    hint_text: "Moyenne 5e"
                    mode: "rectangle"
                
                MDTextField:
                    id: moyenne_4e
                    hint_text: "Moyenne 4e"
                    mode: "rectangle"
                
                MDTextField:
                    id: moyenne_3e
                    hint_text: "Moyenne 3e"
                    mode: "rectangle"
                
                MDRaisedButton:
                    id: lv2
                    text: root.lv2
                    on_release: root.open_menu(self, 'lv2')
                
                MDRaisedButton:
                    id: type_candidat
                    text: root.type_candidat
                    on_release: root.open_menu(self, 'type_candidat')

                MDTextField:
                    id: nombre_fois
                    hint_text: "Nombre de fois"
                    mode: "rectangle"
                
        BoxLayout:
            orientation: 'horizontal'
            spacing: 10
            size_hint_y: None
            height: 60
            MDRaisedButton:
                text: "Sauvegarder"
                md_bg_color: [1, 0.6, 0, 1]  # Orange
                on_release: root.enregistrer_candidat('liste')
            MDRaisedButton:
                text: "Sauvegarder et Continuer"
                md_bg_color: [0, 0.7, 0.5, 1]  # Vert
                on_release: root.enregistrer_candidat('continuer')
"""


class AddCandidat(Screen):
    sexe = StringProperty("M")
    epreuve_facultative = StringProperty("Dessin")
    lv2 = StringProperty("LV2")
    type_candidat = StringProperty("Officiel")
    candidat_id = None  # Stocke l'ID du candidat à modifier

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.menus = {}  # Initialisation vide

    def on_kv_post(self, base_widget):
        # Initialisation des menus après chargement du fichier KV
        self.menus = {
            "sexe": MDDropdownMenu(
                caller=self.ids.sexe,
                items=[
                    {
                        "text": "M",
                        "on_release": lambda x="Masculin": self.set_item("sexe", x),
                    },
                    {
                        "text": "F",
                        "on_release": lambda x="Féminin": self.set_item("sexe", x),
                    },
                ],
                width_mult=3,
            ),
            "epreuve_facultative": MDDropdownMenu(
                caller=self.ids.epreuve_facultative,
                items=[
                    {
                        "text": "Dessin",
                        "on_release": lambda x="Dessin": self.set_item(
                            "epreuve_facultative", x
                        ),
                    },
                    {
                        "text": "Musique",
                        "on_release": lambda x="Musique": self.set_item(
                            "epreuve_facultative", x
                        ),
                    },
                ],
                width_mult=3,
            ),
            "lv2": MDDropdownMenu(
                caller=self.ids.lv2,
                items=[
                    {
                        "text": "LV2",
                        "on_release": lambda x="LV2": self.set_item("lv2", x),
                    },
                    {
                        "text": "PC",
                        "on_release": lambda x="PC": self.set_item("lv2", x),
                    },
                ],
                width_mult=3,
            ),
            "type_candidat": MDDropdownMenu(
                caller=self.ids.type_candidat,
                items=[
                    {
                        "text": "Officiel",
                        "on_release": lambda x="Officiel": self.set_item(
                            "type_candidat", x
                        ),
                    },
                    {
                        "text": "Libre",
                        "on_release": lambda x="Libre": self.set_item(
                            "type_candidat", x
                        ),
                    },
                ],
                width_mult=3,
            ),
        }

    def open_menu(self, caller, menu_type):
        """Ouvre le menu dropdown correspondant"""
        self.menus[menu_type].caller = caller
        self.menus[menu_type].open()

    def set_item(self, item_type, value):
        """Définit la valeur sélectionnée dans le menu"""
        setattr(self, item_type, value)
        self.ids[item_type].text = value
        self.menus[item_type].dismiss()

    def remplir_formulaire(self, candidat):
        """Remplit le formulaire avec les infos du candidat à modifier"""
        self.candidat_id = candidat[0]  # Stocke l'ID pour la mise à jour
        self.ids.prenom.text = candidat[1]
        self.ids.nom.text = candidat[2]
        self.sexe = candidat[3]
        self.ids.date_naissance.text = candidat[4]
        self.ids.lieu_naissance.text = candidat[5]
        self.ids.nationalite.text = candidat[6]
        self.ids.etablissement.text = candidat[7]
        self.ids.aptitude_sportive.text = candidat[8]
        self.epreuve_facultative = candidat[9]
        self.ids.moyenne_6e.text = candidat[10]
        self.ids.moyenne_5e.text = candidat[11]
        self.ids.moyenne_4e.text = candidat[12]
        self.ids.moyenne_3e.text = candidat[13]
        self.lv2 = candidat[14]
        self.type_candidat = candidat[15]
        self.ids.nombre_fois.text = candidat[16]

        # Mise à jour des menus dropdown
        self.menus["sexe"].caller.text = self.sexe
        self.menus["epreuve_facultative"].caller.text = self.epreuve_facultative
        self.menus["lv2"].caller.text = self.lv2
        self.menus["type_candidat"].caller.text = self.type_candidat

    def enregistrer_candidat(self,action):
        """Enregistre ou met à jour un candidat dans la base de données"""
        prenom = self.ids.prenom.text
        nom = self.ids.nom.text
        sexe = self.sexe
        date_naissance = self.ids.date_naissance.text
        lieu_naissance = self.ids.lieu_naissance.text
        nationalite = self.ids.nationalite.text
        etablissement = self.ids.etablissement.text
        aptitude_sportive = self.ids.aptitude_sportive.text
        epr_facultative = self.epreuve_facultative
        moyenne_6e = self.ids.moyenne_6e.text
        moyenne_5e = self.ids.moyenne_5e.text
        moyenne_4e = self.ids.moyenne_4e.text
        moyenne_3e = self.ids.moyenne_3e.text
        lv2 = self.lv2
        type_candidat = self.type_candidat
        nombre_fois = self.ids.nombre_fois.text

        conn = bdd.connect()
        cursor = conn.cursor()

        if self.candidat_id:  # Mise à jour
            cursor.execute(
                """
                UPDATE candidats
                SET prenom=?, nom=?, sexe=?, date_naissance=?, lieu_naissance=?, nationalite=?, etablissement=?, aptitude_sportive=?, epr_facultative=?, moyenne_6e=?, moyenne_5e=?, moyenne_4e=?, moyenne_3e=?, lv2=?, type_candidat=?, nombre_fois=?
                WHERE id=?
            """,
                (
                    prenom,
                    nom,
                    sexe,
                    date_naissance,
                    lieu_naissance,
                    nationalite,
                    etablissement,
                    aptitude_sportive,
                    epr_facultative,
                    moyenne_6e,
                    moyenne_5e,
                    moyenne_4e,
                    moyenne_3e,
                    lv2,
                    type_candidat,
                    nombre_fois,
                    self.candidat_id,
                ),
            )
        else:  # Nouvel enregistrement
            cursor.execute(
                """
                INSERT INTO candidats (prenom, nom, sexe, date_naissance, lieu_naissance, nationalite, etablissement, aptitude_sportive, epr_facultative, moyenne_6e, moyenne_5e, moyenne_4e, moyenne_3e, lv2, type_candidat, nombre_fois)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    prenom,
                    nom,
                    sexe,
                    date_naissance,
                    lieu_naissance,
                    nationalite,
                    etablissement,
                    aptitude_sportive,
                    epr_facultative,
                    moyenne_6e,
                    moyenne_5e,
                    moyenne_4e,
                    moyenne_3e,
                    lv2,
                    type_candidat,
                    nombre_fois,
                ),
            )

        conn.commit()
        conn.close()

        # Vérifie l'action demandée
        if action == "continuer":
           # Réinitialiser le formulaire pour ajouter un autre candidat
           self.ids.prenom.text = ""
           self.ids.nom.text = ""
           self.sexe = "M"
           self.ids.date_naissance.text = ""
           self.ids.lieu_naissance.text = ""
           self.ids.nationalite.text = ""
           self.ids.etablissement.text = ""
           self.ids.aptitude_sportive.text = ""
           self.epreuve_facultative = "Dessin"
           self.ids.moyenne_6e.text = ""
           self.ids.moyenne_5e.text = ""
           self.ids.moyenne_4e.text = ""
           self.ids.moyenne_3e.text = ""
           self.lv2 = "LV2"
           self.type_candidat = "Officiel"
           self.ids.nombre_fois.text = ""
        elif action == "liste":
           # Redirection vers la liste des candidats
           self.manager.current = "ListeCandidats"
           self.manager.get_screen("ListeCandidats").load_candidats()
           self.manager.get_screen("ListeCandidats").afficher_candidats()


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)


if __name__ == "__main__":
    MyApp().run()
