import os
import sys
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), "../../../.."))
)

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivy.metrics import dp
from bfem.database.candidat import Candidat

class ListeMeriteScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.candidat = Candidat()
        self.create_data_table()

    def create_data_table(self):
        # Récupérer les données des candidats
        liste_candidats = self.candidat.get_all_candidate()
        
        # Préparer les données pour la table
        rows_data = []
        for candidat in liste_candidats:
            # Créer un bouton d'impression pour chaque candidat
            rows_data.append((
                candidat[1],  # Prénom
                candidat[2],  # Nom
                candidat[5],  # Sexe
                candidat[3],  # Date de naissance
                candidat[9],  # Établissement
                str(candidat[10]) if len(candidat) > 10 and candidat[10] is not None else "",  # Moyenne
                "Imprimer le relevé"  # Indicateur pour le bouton d'impression
            ))

        # Créer la table de données
        self.data_table = MDDataTable(
            size_hint=(1, 0.9),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ("Prénom", dp(30)),
                ("Nom", dp(30)),
                ("Sexe", dp(20)),
                ("Naissance", dp(30)),
                ("Établissement", dp(40)),
                ("Moyenne", dp(20)),
                ("Relevé", dp(20))
            ],
            row_data=rows_data,
            use_pagination=True,
            check=False,
            rows_num=10,
            background_color_header="#256D94",
            background_color_selected_cell="#E0E0E0"
        )
        
        # Lier l'événement de clic sur le bouton d'impression
        self.data_table.bind(on_row_press=self.on_print_button_press)
        
        # Ajouter la table au layout
        layout = MDBoxLayout(orientation='vertical')
        layout.add_widget(self.data_table)
        self.add_widget(layout)

    def on_print_button_press(self, instance, row):
        try:
            # Vérifier si le dernier élément de la ligne est "print"
            if row.data[-1] == "print":
                # Récupérer les informations du candidat (les éléments précédant "print")
                candidat_info = row.data[:-1]
                
                # Afficher un message de confirmation (vous pouvez remplacer par votre logique d'impression)
                print(f"Impression du relevé pour {candidat_info[0]} {candidat_info[1]}")
                
                # Appelez ici votre méthode d'impression si elle existe
                # Par exemple : self.candidat.imprimer_releve(candidat_info)
        except Exception as e:
            print(f"Erreur lors de l'impression : {e}")

class ListeMeriteApp(MDApp):
    def build(self):
        # Créer le gestionnaire d'écran
        self.sm = MDScreenManager()
        
        # Ajouter l'écran Liste de Mérite
        liste_merite_screen = ListeMeriteScreen(name='liste_merite')
        self.sm.add_widget(liste_merite_screen)
        
        return self.sm

    def on_start(self):
        # Personnaliser le thème si nécessaire
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"

if __name__ == '__main__':
    ListeMeriteApp().run()