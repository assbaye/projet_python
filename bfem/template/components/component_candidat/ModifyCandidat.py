from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), "../../../.."))
)

from bfem.database.candidat import Candidat
from bfem.database.bdd import bdd
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.pickers import MDDatePicker
from bfem.database.candidat import Candidat
from bfem.database.livret_scolaire import LivretScolaire

KV = """
<ModifyCandidat>:
    name: "modify_candidat"
    sexe: "M"
    epreuve_facultative: "Dessin"
    lv2: "LV2"
    type_candidat: "Officiel"
    
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 20
        padding: [20, 20, 20, 20]
    
        MDBoxLayout:
            orientation: 'vertical'
            spacing: 20

            MDLabel:
                id: state_modify
                halign: "center"
                size_hint: 1, None
                height: 50
                pos_hint: {'top': 1}

            ScrollView:
                padding: ('10dp', '10dp', '10dp', '10dp')
        
                MDGridLayout:
                    cols: 2
                    spacing: 40
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
                        on_focus: if self.focus: root.show_date_picker()
                    
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
                        on_focus: if self.focus: root.open_menu(self, "aptitude_sportive")
                    
                    MDTextField:
                        id: sexe
                        hint_text: "Sexe"
                        mode: "rectangle"
                        on_focus: if self.focus: root.open_menu(self, "sexe") 
                
                    MDTextField:
                        id: epreuve_facultative
                        hint_text: "Epreuves facultative"
                        mode: "rectangle"
                        on_focus: if self.focus: root.open_menu(self, "epreuve_facultative") 
                
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
                    
                    MDTextField:
                        id: lv2
                        hint_text: "Pc/lv2"
                        mode: "rectangle"
                        on_focus: if self.focus: root.open_menu(self, "lv2") 
                
                    MDTextField:
                        id: type_candidat
                        hint_text: "Type de Candidat"
                        mode: "rectangle"
                        on_focus: if self.focus: root.open_menu(self, "type_candidat") 
                
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
                text: "Annuler"
                md_bg_color: [0.7, 0.1, 0.1, 1]  # Rouge
                on_release: root.cancel_modification()
            MDRaisedButton:
                text: "Mettre à jour"
                md_bg_color: [0, 0.7, 0.5, 1]  # Vert
                on_release: root.update_candidat()
"""
Builder.load_string(KV)

class ModifyCandidat(MDScreen):
    sexe = StringProperty("M")
    epreuve_facultative = StringProperty("Dessin")
    lv2 = StringProperty("LV2")
    type_candidat = StringProperty("Officiel")
    candidat_id = None  # Stocke l'ID du candidat à modifier
    livret_id = None  # Stocke l'ID du livret scolaire à modifier

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # Initialisation des menus
    def on_kv_post(self, *args):
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
                        "text": "Neutre",
                        "on_release": lambda x="Neutre": self.set_item(
                            "epreuve_facultative", x
                        ),
                    },
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
            "aptitude_sportive": MDDropdownMenu(
                caller=self.ids.aptitude_sportive,
                items=[
                    {
                        "text": "Apte",
                        "on_release": lambda x="Apte": self.set_item(
                            "aptitude_sportive", x
                        ),
                    },
                    {
                        "text": "Inapte",
                        "on_release": lambda x="Inapte": self.set_item(
                            "aptitude_sportive", x
                        ),
                    },
                ],
                width_mult=3,
            ),
        }
       
    def open_menu(self, caller, menu_type):
        if menu_type in self.menus:
            self.menus[menu_type].caller = caller  # Associez le caller
            self.menus[menu_type].open()  # Ouvrez le menu
        else:
            print(f"Erreur : le menu '{menu_type}' n'existe pas.")

    def set_item(self, item_type, value):
        """Définit la valeur sélectionnée dans le menu"""
        setattr(self, item_type, value)
        self.ids[item_type].text = value
        self.menus[item_type].dismiss()

    def load_candidat_data(self, candidat_id):
        """Charge les données du candidat à modifier"""
        self.candidat_id = candidat_id
        
        try:
            # Récupérer les données du candidat
            interface_candidat = Candidat()
            candidat_data = interface_candidat.get_candidat_by_id(candidat_id)
            
            if not candidat_data:
                self.ids.state_modify.text = "Erreur: Candidat non trouvé"
                return
            
            # Récupérer les données du livret scolaire
            interface_livret = LivretScolaire()
            livret_data = interface_livret.get_livret_by_candidat_id(candidat_id)
            
            if not livret_data:
                self.ids.state_modify.text = "Erreur: Livret scolaire non trouvé"
                return
                
            self.livret_id = livret_data[0][0]  # Supposant que l'ID est le premier élément
            
            # Remplir le formulaire avec les données
            self.remplir_formulaire(candidat_data[0], livret_data[0])
            
        except Exception as e:
            print(f"Erreur lors du chargement des données: {e}")
            self.ids.state_modify.text = f"Erreur: {str(e)}"

    def remplir_formulaire(self, candidat, livret):
        """Remplit le formulaire avec les infos du candidat et du livret scolaire"""
        # Données du candidat
        self.ids.prenom.text = candidat[1]  # ajuster les indices selon votre structure de données
        self.ids.nom.text = candidat[2]
        self.ids.sexe.text = "M" if candidat[3] == "H" else "F"
        self.sexe = "Masculin" if candidat[3] == "H" else "Féminin"
        self.ids.date_naissance.text = candidat[4]
        self.ids.lieu_naissance.text = candidat[5]
        self.ids.nationalite.text = candidat[6]
        self.ids.etablissement.text = candidat[7]
        self.ids.aptitude_sportive.text = candidat[8]
        self.ids.epreuve_facultative.text = candidat[9]
        self.epreuve_facultative = candidat[9]
        self.ids.lv2.text = candidat[10]
        self.lv2 = candidat[10]
        self.ids.type_candidat.text = candidat[11]
        self.type_candidat = candidat[11]
        
        # Données du livret scolaire
        self.ids.nombre_fois.text = str(livret[1])
        self.ids.moyenne_6e.text = str(livret[2])
        self.ids.moyenne_5e.text = str(livret[3])
        self.ids.moyenne_4e.text = str(livret[4])
        self.ids.moyenne_3e.text = str(livret[5])

    def show_date_picker(self):
        """Affiche le sélecteur de date"""
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_date_selected)
        date_dialog.open()

    def on_date_selected(self, instance, value, date_range):
        """Traite la date sélectionnée"""
        self.ids.date_naissance.text = str(value)

    def validate_fields(self):
        """Valide les champs du formulaire"""
        valited = True

        # Vérifier que tous les champs sont remplis
        for field in [
            "prenom", "nom", "type_candidat", "epreuve_facultative", "date_naissance", 
            "lieu_naissance", "nationalite", "etablissement", "aptitude_sportive",
            "moyenne_6e", "moyenne_5e", "sexe", "lv2", "moyenne_4e", "moyenne_3e", "nombre_fois"
        ]:
            if getattr(self.ids, field).text == "":
                field_obj = getattr(self.ids, field)
                field_obj.error = True
                field_obj.helper_text_mode = "on_error"
                field_obj.helper_text = "Veuillez remplir ce champ"
                valited = False

        # Vérifier que les moyennes sont entre 0 et 20
        if valited:
            for field in ["moyenne_6e", "moyenne_5e", "moyenne_4e", "moyenne_3e"]:
                try:
                    value = float(getattr(self.ids, field).text)
                    if value > 20 or value < 0:
                        field_obj = getattr(self.ids, field)
                        field_obj.error = True
                        field_obj.helper_text_mode = "on_error"
                        field_obj.helper_text = "Moyenne doit être entre 0 et 20"
                        valited = False
                except ValueError:
                    field_obj = getattr(self.ids, field)
                    field_obj.error = True
                    field_obj.helper_text_mode = "on_error"
                    field_obj.helper_text = "Veuillez entrer un nombre valide"
                    valited = False

        return valited

    def update_candidat(self):
        """Met à jour les informations du candidat et du livret scolaire"""
        if not self.validate_fields():
            return
            
        try:
            # Préparer les données du candidat
            prenom = self.ids.prenom.text
            nom = self.ids.nom.text
            sexe = "H" if self.sexe == "Masculin" else "F"
            date_naissance = self.ids.date_naissance.text
            lieu_naissance = self.ids.lieu_naissance.text
            nationalite = self.ids.nationalite.text
            etablissement = self.ids.etablissement.text
            aptitude_sportive = self.ids.aptitude_sportive.text
            epr_facultative = self.epreuve_facultative
            lv2 = self.lv2
            type_candidat = self.type_candidat
            
            # Préparer les données du livret scolaire
            nombre_fois = self.ids.nombre_fois.text
            moyenne_6e = self.ids.moyenne_6e.text
            moyenne_5e = self.ids.moyenne_5e.text
            moyenne_4e = self.ids.moyenne_4e.text
            moyenne_3e = self.ids.moyenne_3e.text
            
            # Mettre à jour le candidat
            interface_candidat = Candidat()
            interface_candidat.update_candidat(
                self.candidat_id, prenom, nom, date_naissance, lieu_naissance, 
                sexe, nationalite, epr_facultative, etablissement, 
                aptitude_sportive, lv2, type_candidat
            )
            
            # Mettre à jour le livret scolaire
            interface_livret = LivretScolaire()
            interface_livret.update_livret(
                self.livret_id, nombre_fois, moyenne_6e, 
                moyenne_5e, moyenne_4e, moyenne_3e
            )
            
            # Afficher le message de succès
            self.ids.state_modify.text = "Candidat modifié avec succès"
            
            # Mettre à jour la liste des candidats
            liste_screen = self.manager.get_screen("ListeCandidat")
            liste_screen.load_candidats()
            
            # Retourner à la liste des candidats après un court délai
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.go_to_list(), 1.5)
            
        except Exception as e:
            print(f"Erreur lors de la mise à jour: {e}")
            self.ids.state_modify.text = f"Erreur de mise à jour: {str(e)}"

    def cancel_modification(self):
        """Annule la modification et retourne à la liste des candidats"""
        self.go_to_list()

    def go_to_list(self):
        """Retourne à l'écran de liste des candidats"""
        self.manager.current = "ListeCandidat"