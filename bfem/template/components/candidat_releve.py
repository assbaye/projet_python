from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Définition du style KV
kv = '''
<ListeCandidats>:
    orientation: 'vertical'
    padding: 10
    spacing: 10

    # En-tête
    BoxLayout:
        size_hint_y: None
        height: 50
        Label:
            text: 'Liste des Candidats - BFEM '
            font_size: '24sp'
            bold: True
            size_hint_x: 0.8

    # En-têtes du tableau
    BoxLayout:
        size_hint_y: None
        height: 40
        canvas.before:
            Color:
                rgba: 0.2, 0.5, 0.9, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        Label:
            text: 'N° Table'
            bold: True
            size_hint_x: 0.1
        Label:
            text: 'Nom et Prénom'
            bold: True
            size_hint_x: 0.2
        Label:
            text: 'Sexe'
            bold: True
            size_hint_x: 0.1
        Label:
            text: 'Date Naissance'
            bold: True
            size_hint_x: 0.15
        Label:
            text: 'Lieu Naissance'
            bold: True
            size_hint_x: 0.2
        Label:
            text: 'Établissement'
            bold: True
            size_hint_x: 0.15
        Label:
            text: 'Actions'
            bold: True
            size_hint_x: 0.1

    # Corps du tableau avec scroll
    ScrollView:
        GridLayout:
            id: tableau_body
            cols: 1
            spacing: 2
            size_hint_y: None
            height: self.minimum_height

<CandidatRow@BoxLayout>:
    size_hint_y: None
    height: 40
    canvas.before:
        Color:
            rgba: 0.25, 0.25, 0.25, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        id: numero
        size_hint_x: 0.1
    Label:
        id: nom_prenom
        size_hint_x: 0.2
    Label:
        id: sexe
        size_hint_x: 0.1
    Label:
        id: date_naissance
        size_hint_x: 0.15
    Label:
        id: lieu_naissance
        size_hint_x: 0.2
    Label:
        id: etablissement
        size_hint_x: 0.15
    Button:
        size_hint_x: 0.1
        text: 'Imprimer'
        background_color: 0.3, 0.6, 1, 1
        on_press: app.root.imprimer_releve(root.candidat['numero'])
'''

# Chargement du style KV
Builder.load_string(kv)

class ListeCandidats(BoxLayout):
    tableau_candidats = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.charger_candidats()
    
    def charger_candidats(self):
        # Données exemple (à remplacer par les données de la base de données)
        self.candidats = [
            {
                "numero": "001",
                "nom": "DIOP",
                "prenom": "Fatou",
                "sexe": "F",
                "date_naissance": "15/03/2008",
                "lieu_naissance": "Dakar",
                "etablissement": "CEM Pikine"
            },
            {
                "numero": "002",
                "nom": "FALL",
                "prenom": "Amadou",
                "sexe": "M",
                "date_naissance": "22/06/2007",
                "lieu_naissance": "Thiès",
                "etablissement": "CEM Thiès"
            },
            {
                "numero": "003",
                "nom": "NDIAYE",
                "prenom": "Marie",
                "sexe": "F",
                "date_naissance": "10/01/2008",
                "lieu_naissance": "Saint-Louis",
                "etablissement": "CEM Saint-Louis"
            }
        ]
        self.actualiser_tableau()
    
    def actualiser_tableau(self):
       
        
        self.ids.tableau_body.clear_widgets()
        
        # Ajouter chaque candidat au tableau
        for candidat in self.candidats:
            self.ids.tableau_body.add_widget(CandidatRow(candidat))
    
    def imprimer_releve(self, numero_table):
        print(f"Impression du relevé pour le candidat N°{numero_table}")
        # la logique d'impression du relevé

class CandidatRow(BoxLayout):
    def __init__(self, candidat, **kwargs):
        super().__init__(**kwargs)
        self.candidat = candidat
        self.ids.numero.text = candidat['numero']
        self.ids.nom_prenom.text = f"{candidat['nom']} {candidat['prenom']}"
        self.ids.sexe.text = candidat['sexe']
        self.ids.date_naissance.text = candidat['date_naissance']
        self.ids.lieu_naissance.text = candidat['lieu_naissance']
        self.ids.etablissement.text = candidat['etablissement']

class ListeCandidatsApp(App):
    def build(self):
        return ListeCandidats()
