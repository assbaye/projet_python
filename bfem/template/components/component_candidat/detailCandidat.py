from kivymd.uix.backdrop.backdrop import MDBoxLayout
import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), "../../../.."))
)

from bfem.database.candidat import Candidat
from bfem.database.livret_scolaire import LivretScolaire
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.app import MDApp
from kivy.properties import StringProperty, ListProperty

KV = """
<DetailCandidat>:
    name: "detail_candidat"
    
    MDBoxLayout:
        orientation: 'vertical'
        spacing: 20
        padding: [20, 20, 20, 20]
        
        MDTopAppBar:
            title: "Détails du candidat"
            elevation: 4
            left_action_items: [["arrow-left", lambda x: root.retour_liste()]]
        
        ScrollView:
            
            MDBoxLayout:
                orientation: 'vertical'
                spacing: 20
                adaptive_height: True
                padding: [10, 10, 10, 10]
                
                # Carte d'information personnelle
                MDCard:
                    orientation: 'vertical'
                    padding: 16
                    spacing: 16
                    elevation: 2
                    size_hint: 1, None
                    height: self.minimum_height
                    
                    MDLabel:
                        text: "Informations personnelles"
                        font_style: "H5"
                        size_hint_y: None
                        height: self.texture_size[1]
                        
                    MDGridLayout:
                        cols: 2
                        spacing: [20, 20]
                        adaptive_height: True
                        
                        MDLabel:
                            text: "Nom:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: nom
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Prénom:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: prenom
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Sexe:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: sexe
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Date de naissance:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: date_naissance
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Lieu de naissance:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: lieu_naissance
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Nationalité:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: nationalite
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                
                # Carte d'information scolaire
                MDCard:
                    orientation: 'vertical'
                    padding: 16
                    spacing: 16
                    elevation: 2
                    size_hint: 1, None
                    height: self.minimum_height
                    
                    MDLabel:
                        text: "Informations scolaires"
                        font_style: "H5"
                        size_hint_y: None
                        height: self.texture_size[1]
                        
                    MDGridLayout:
                        cols: 2
                        spacing: [20, 20]
                        adaptive_height: True
                        
                        MDLabel:
                            text: "Établissement:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: etablissement
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Type de candidat:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: type_candidat
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Aptitude sportive:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: aptitude_sportive
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Épreuve facultative:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: epreuve_facultative
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "LV2/PC:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: lv2
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Nombre de fois:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: nombre_fois
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                
                # Carte des moyennes
                MDCard:
                    orientation: 'vertical'
                    padding: 16
                    spacing: 16
                    elevation: 2
                    size_hint: 1, None
                    height: self.minimum_height
                    
                    MDLabel:
                        text: "Moyennes scolaires"
                        font_style: "H5"
                        size_hint_y: None
                        height: self.texture_size[1]
                        
                    MDGridLayout:
                        cols: 2
                        spacing: [20, 20]
                        adaptive_height: True
                        
                        MDLabel:
                            text: "Moyenne 6e:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: moyenne_6e
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Moyenne 5e:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: moyenne_5e
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Moyenne 4e:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: moyenne_4e
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Moyenne 3e:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: moyenne_3e
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                            
                        MDLabel:
                            text: "Moyenne générale:"
                            bold: True
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDLabel:
                            id: moyenne_generale
                            text: ""
                            size_hint_y: None
                            height: self.texture_size[1]
                
                # Actions
                MDBoxLayout:
                    orientation: 'horizontal'
                    spacing: 10
                    size_hint_y: None
                    height: 60
                    padding: [0, 20, 0, 0]
                    pos_hint: {'center_x': 0.5}
                    
                    MDFillRoundFlatButton:
                        text: "Modifier"
                        md_bg_color: [0, 0.7, 0.5, 1]  # Vert
                        on_release: root.modifier_candidat()
                    
                    MDFillRoundFlatButton:
                        text: "Imprimer fiche"
                        md_bg_color: [0.2, 0.4, 0.8, 1]  # Bleu
                        on_release: root.imprimer_fiche()
                    
                    MDFillRoundFlatButton:
                        text: "Supprimer"
                        md_bg_color: [0.8, 0.2, 0.2, 1]  # Rouge
                        on_release: root.confirmer_suppression()
"""
Builder.load_string(KV)

class DetailCandidat(MDScreen):
    candidat_id = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def load_candidat_data(self, candidat_id):
        """Charge les données du candidat à afficher"""
        self.candidat_id = candidat_id
        
        try:
            # Récupérer les données du candidat
            interface_candidat = Candidat()
            candidat_data = interface_candidat.get_candidate(candidat_id)
            
            if not candidat_data:
                print("Erreur: Candidat non trouvé")
                return
            
            # Récupérer les données du livret scolaire
            interface_livret = LivretScolaire()
            livret_data = interface_livret.get_livret_by_candidat_id(candidat_id)
            
            if not livret_data:
                print("Erreur: Livret scolaire non trouvé")
                return
                
            # Afficher les données du candidat
            self.afficher_details(candidat_data[0], livret_data[0])
            
        except Exception as e:
            print(f"Erreur lors du chargement des données: {e}")
    
    def afficher_details(self, candidat, livret):
        """Affiche les détails du candidat dans l'interface"""
        # Informations personnelles
        self.ids.nom.text = candidat[2]  # Ajuster les indices selon votre structure de données
        self.ids.prenom.text = candidat[1]
        self.ids.sexe.text = "Masculin" if candidat[3] == "H" else "Féminin"
        self.ids.date_naissance.text = candidat[4]
        self.ids.lieu_naissance.text = candidat[5]
        self.ids.nationalite.text = candidat[6]
        
        # Informations scolaires
        self.ids.etablissement.text = candidat[7]
        self.ids.type_candidat.text = candidat[11]
        self.ids.aptitude_sportive.text = candidat[8]
        self.ids.epreuve_facultative.text = candidat[9]
        self.ids.lv2.text = candidat[10]
        
        # Données du livret scolaire
        self.ids.nombre_fois.text = str(livret[1])
        self.ids.moyenne_6e.text = str(livret[2])
        self.ids.moyenne_5e.text = str(livret[3])
        self.ids.moyenne_4e.text = str(livret[4])
        self.ids.moyenne_3e.text = str(livret[5])
        
        # Calculer la moyenne générale
        try:
            moyenne_generale = (float(livret[2]) + float(livret[3]) + float(livret[4]) + float(livret[5])) / 4
            self.ids.moyenne_generale.text = f"{moyenne_generale:.2f}"
        except (ValueError, TypeError):
            self.ids.moyenne_generale.text = "Non disponible"
    
    def retour_liste(self):
        """Retourne à l'écran de liste des candidats"""
        self.manager.current = "ListeCandidat"
    
    def modifier_candidat(self):
        """Ouvre l'écran de modification pour ce candidat"""
        modify_screen = self.manager.get_screen("modify_candidat")
        modify_screen.load_candidat_data(self.candidat_id)
        self.manager.current = "modify_candidat"
    
   
    def confirmer_suppression(self):
        """Demande confirmation avant de supprimer le candidat"""
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton
        
        self.dialog = MDDialog(
            title="Confirmation de suppression",
            text="Êtes-vous sûr de vouloir supprimer ce candidat ? Cette action est irréversible.",
            buttons=[
                MDFlatButton(
                    text="ANNULER",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.dialog.dismiss()
                ),
                MDFlatButton(
                    text="SUPPRIMER",
                    theme_text_color="Custom",
                    text_color=(0.8, 0.2, 0.2, 1),  # Rouge
                    on_release=lambda x: self.supprimer_candidat()
                ),
            ],
        )
        self.dialog.open()
    
    def supprimer_candidat(self):
        """Supprime le candidat de la base de données"""
        try:
            self.dialog.dismiss()
            
            # Supprimer d'abord le livret scolaire (contrainte de clé étrangère)
            interface_livret = LivretScolaire()
            interface_livret.delete_livretscolaire(self.candidat_id)
            
            # Puis supprimer le candidat
            interface_candidat = Candidat()
            interface_candidat.delete_candidate(self.candidat_id)
            
            # Afficher un message de confirmation
            from kivymd.uix.snackbar import Snackbar
            Snackbar(text="Candidat supprimé avec succès").open()
            
            # Mettre à jour la liste des candidats
            liste_screen = self.manager.get_screen("ListeCandidat")
            liste_screen.load_candidats()
            
            # Retourner à la liste
            self.retour_liste()
            
        except Exception as e:
            print(f"Erreur lors de la suppression: {e}")
            from kivymd.uix.snackbar import Snackbar
            Snackbar(text=f"Erreur: {str(e)}").open()