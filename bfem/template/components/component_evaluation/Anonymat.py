from kivy.uix.accordion import StringProperty
from kivy.uix.gesturesurface import GestureContainer
from kivy.uix.accordion import ListProperty
from kivymd.uix.datatables.datatables import MDDropdownMenu
from kivymd.uix.banner.banner import MDFlatButton
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
import sys
import os
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import webbrowser
from kivy.lang import Builder 
from .ListAnonymat import ListAnonymat
from random import randint

# Chemin d'accès à la base de données
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), "../../../..")))
from bfem.database.anonymous import AnonymatDatabase
from bfem.database.matiere import Matiere
from bfem.database.candidat import Candidat

KV = """
<Anonymat> :
    MDNavigationLayout:

        MDScreenManager:
            id:screen_manager
            MDScreen:
                MDBoxLayout:
                    orientation:"vertical"
                    padding: ('10dp', '10dp', '10dp', '10dp')
                    # md_bg_color:"#000000"
                    MDBoxLayout:
                        id: box_nav
                        orientation:"horizontal"
                        height: dp(60)
                        size_hint: 1, None
                        pos_hint: {'top': 1,}
                        # md_bg_color:"#000000"
                        spacing: '10dp'
                        padding:(    '10dp', '10dp', '10dp', '10dp')
                        MDBoxLayout:
                            id:navigation
                            orientation:"horizontal"
                            spacing: '10dp'
                            size_hint_x: None
                        Widget:
                            size_hint_x:0.6

                        MDBoxLayout:
                            id: nav_plus
                            orientation:"horizontal"
                            # md_bg_color:"#ffffff"
                        
                            size_hint: None,None
                            height:100
                            
                            # spacing: '10dp'
                            # padding:(    '30dp', '10dp', '10dp', '0dp')
                            MDTextField:
                                id:selected_matiere
                                hint_text:"Matiere"
                                size_hint:[1,None]
                                height: "40dp"
                                readonly: True
                                width:200
                               
                                on_focus:if self.focus: root.show_dropdown(self)
                                pos_hint:{"bottom": 1}
            
                        
                       
                    ScreenManager:
                        id:screen_manager_current
                        ListAnonymat:
                            name: "ListAnonymat"
                            id:listano
                       
                
"""


            
# kv = """
# <Anonymat>:
#     BoxLayout:
#         orientation: 'vertical'
#         padding: [20, 20, 20, 20]
#         spacing: 20
#         canvas.before:
#             Color:
#                 rgba: 0.9, 0.95, 1, 1
#             RoundedRectangle:
#                 pos: self.pos
#                 size: self.size
#                 radius: [20]

#         BoxLayout:
#             size_hint_y: None
#             height: dp(50)
#             spacing: 10
#             padding: [0, 0, 0, 0]  
#             pos_hint: {"top": 1}

#             MDDropDownItem:
#                 id: matiere_spinner
#                 pos_hint: {"center_y": .5}
#                 on_release: app.update_table(self.text)  # Met à jour le tableau avec la matière sélectionnée

            
#             Widget:  # Espace flexible pour pousser les boutons à droite
            
#             MDRaisedButton:
#                 text: "Générer"
#                 md_bg_color: 0, 0.7, 0.6, 1
#                 on_release: app.generer_anonymats()
            
#             MDRaisedButton:
#                 text: "Imprimer"
#                 md_bg_color: 1, 0.75, 0, 1
#                 on_release: app.imprimer_anonymats()

#         MDCard:
#             orientation: 'vertical'
#             padding: [10, 10, 10, 10]
#             radius: [20]
#             elevation: 4

#             BoxLayout:
#                 size_hint_y: None
#                 height: dp(40)
#                 MDLabel:
#                     text: "Numéro de tableau"
#                     bold: True
#                 MDLabel:
#                     text: "Anonymat"
#                     bold: True

#             ScrollView:
#                 BoxLayout:
#                     id: table_container
#                     orientation: 'vertical'
#                     size_hint_y: None
#                     height: self.minimum_height
# """

Builder.load_string(KV)
class Anonymat(MDScreen):
    matiere_id = StringProperty('')
    listAnonymat_matiere = ListProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def on_kv_post(self, base_widget):
        box_layout = self.ids.navigation
        current_screen = self.ids.screen_manager_current

         # Liste des éléments de navigation
        self.list_navigation = [
            {
                "text": "Liste des anonymats",
                "icon": "book-plus",
                "screen": ListAnonymat(name="Liste Anonymat")
            },
             
        ]
        # Ajouter chaque écran dans le ScreenManager
        for nav in self.list_navigation:
            current_screen.add_widget(nav["screen"])

        # Créer les boutons pour chaque élément de navigation
        for nav in self.list_navigation:
            bouton_navigation = MDFlatButton(
                icon=nav["icon"],
                text=nav["text"],
                md_bg_color="#256D94",
                theme_text_color="Custom",
                text_color="#ffffff",
               
               
            )
            box_layout.add_widget(bouton_navigation)
        
        imprimer = MDFlatButton(
            text="Imprimer",
            icon="printer",
            md_bg_color="#44B3B1",
            theme_text_color="Custom",
            text_color="#ffffff",
            
        )
        box_layout.add_widget(imprimer)
        Generer = MDFlatButton(
            id="generer_action",
            text="Generer",
            icon="printer",
            md_bg_color="#44B3B1",
            theme_text_color="Custom",
            text_color="#ffffff",
            
            
        )
        Generer.bind(on_release=lambda instance: self.generer_anonymats())

        box_layout.add_widget(Generer)
    # def generer_anonymat(self):

    def open_menu(self,text_field):
        print("IDs disponibles:", self.parent)
        interface_matiere = Matiere()
        menu_items = [
            {"text": matiere, "viewclass": "OneLineListItem", "on_release": lambda x=matiere: self.select_matiere(x)}
            for matiere in interface_matiere.getAll()
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.selected_matiere,
            items=menu_items,
            width_mult=4
        )
        self.menu.open()

    def select_matiere(self, matiere):
        self.root.ids.selected_matiere.text = matiere
        self.menu.dismiss()
        
        # self.afficher_notes(matiere)  # Affichage automatique des notes
 
    def show_dropdown(self, textfield):
        """Affiche le menu déroulant sous le champ MDTextField."""
        matiere = Matiere()
        if not textfield:  # Vérification si textfield est valide
            print("Erreur: textfield est None")
            return
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": mat[1],
                "on_release": lambda x=mat: self.set_matiere(textfield, x[1],x[0]),
            } for mat in matiere.getAll()
        ]
        
        self.menu = MDDropdownMenu(
            caller=textfield,
            items=menu_items,
            width_mult=4,
        )
       
        if self.menu:
            self.menu.open()

    def set_matiere(self, textfield, value,id):

        self.matiere_id = str(id)
        if not hasattr(self, 'ids') or 'listano' not in self.ids:
            print("Erreur: ID 'listenote' non trouvé")
            return
        textfield.text = value
        self.ids.listano.set_matiere(str(id))

        if self.menu:
            self.menu.dismiss()

    # def afficher_notes(self):
    #     matiere = self.root.ids.selected_matiere.text
    #     notes_list = self.root.ids.notes_list
    #     notes_list.clear_widgets()
        
    #     if matiere and matiere in self.matieres_notes:
    #         for note in self.matieres_notes[matiere]:
    #             notes_list.add_widget(OneLineListItem(text=f"Note : {note}"))
    #     else:
    #         notes_list.add_widget(OneLineListItem(text="Aucune note disponible"))


   
    # def on_start(self):
    #     # Charger les matières dans le Spinner
    #     matieres = self.anonymat_db.get_matieres()
    #     matiere_spinner = self.root.ids.matiere_spinner

    #     # Ajouter toutes les matières dans le Spinner
    #     if matieres:
    #         matiere_spinner.values = matieres
    #         matiere_spinner.text = matieres[0]  # Sélectionner la première matière par défaut
    #         self.update_table(matieres[0])  # Charger les anonymats pour la première matière
    #     else:
    #         matiere_spinner.text = "Aucune matière"

    # def update_table(self, selected_matiere):
    #     """ Met à jour le tableau avec les anonymats de la matière sélectionnée """
    #     if selected_matiere:
    #         anonymats = self.anonymat_db.afficher_anonymats(selected_matiere)
    #         container = self.root.ids.table_container
    #         container.clear_widgets()

    #         for candidat_id, numero_anonymat in anonymats:
    #             row = BoxLayout(size_hint_y=None, height=dp(40))
    #             row.add_widget(MDLabel(text=str(candidat_id), size_hint_x=0.5))
    #             row.add_widget(MDLabel(text=str(numero_anonymat), size_hint_x=0.5))
    #             container.add_widget(row)



    def generer_anonymats(self,*arg,):

        interface_ano = AnonymatDatabase()
        selected_matiere = self.ids.selected_matiere.text
       
          
        print(self.matiere_id)
        if  self.matiere_id :
           
            allcanidats = Candidat().get_all_candidate()
                # allmatiere = Matiere().getAll()
                
            for candidat in allcanidats:
               
               stat = interface_ano.generer_anonymat(candidat_id=candidat[0],matiere_id=self.matiere_id,examen="1")
               print(stat)
            self.ids.listano.set_matiere(self.matiere_id)

        else :
                print("error")
            # self.anonymat_db.generer_anonymats(selected_matiere)
        
            # # Étape 2 : Récupérer les anonymats mis à jour
            # anonymats = self.anonymat_db.afficher_anonymats(selected_matiere)
        
            # # Étape 3 : Afficher les anonymats dans le tableau
            # container = self.root.ids.table_container
            # container.clear_widgets()

            # for candidat_id, numero_anonymat in anonymats:
            #     row = BoxLayout(size_hint_y=None, height=dp(40))
            #     row.add_widget(MDLabel(text=str(candidat_id), size_hint_x=0.5))
            #     row.add_widget(MDLabel(text=str(numero_anonymat), size_hint_x=0.5))
            #     container.add_widget(row)


   

    def imprimer_anonymats(self):
        container = self.root.ids.table_container
        if container.children:
            print("Début de l'impression...")  # Message de débogage

            # Création du PDF
            pdf_file = "anonymats.pdf"
            try:
                doc = SimpleDocTemplate(pdf_file, pagesize=A4)
                elements = []

                # Ajouter un titre
                title = [["Liste des Anonymats"]]
                title_table = Table(title)
                title_table.setStyle(TableStyle([
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 18),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
                ]))
                elements.append(title_table)
                elements.append(Table([[" "]]))  # Espace entre le titre et le tableau

                # Ajouter les en-têtes du tableau
                data = [["Numéro de tableau", "Anonymat"]]

                # Récupérer les anonymats affichés dans le tableau
                for row in reversed(container.children):
                    candidat_id = row.children[1].text  # Le texte du premier MDLabel
                    numero_anonymat = row.children[0].text  # Le texte du second MDLabel
                    print(f"Ajout au PDF : {candidat_id}, {numero_anonymat}")  # Débogage
                    data.append([candidat_id, numero_anonymat])

                # Créer le tableau pour le PDF
                table = Table(data)
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 14),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ]))
                elements.append(table)

                # Génération du PDF
                doc.build(elements)
                print(f"PDF généré : {pdf_file}")

                # Ouvrir le PDF (multiplateforme)
                webbrowser.open_new(pdf_file)

            except Exception as e:
                print(f"Erreur lors de la génération du PDF : {e}")
        else:
            print("Aucun anonymat à imprimer.")

# class Example(MDApp):
#     def build(self):
#         return Anonymat()

# if __name__ == '__main__':
#     Example().run()
