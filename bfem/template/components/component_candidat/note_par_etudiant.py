from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.lang import Builder

# Définition de l'interface principale
class NotesParCandidat(BoxLayout):
    # Propriétés du candidat
    numero_table = StringProperty("")
    prenom = StringProperty("")
    nom = StringProperty("")
    date_naissance = StringProperty("")
    lieu_naissance = StringProperty("")
    
    # Notes avec leurs coefficients
    note_compo_franc = NumericProperty(0)
    note_dictee = NumericProperty(0)
    note_etude_texte = NumericProperty(0)
    note_inst_civique = NumericProperty(0)
    note_hist_geo = NumericProperty(0)
    note_maths = NumericProperty(0)
    note_pc_lv2 = NumericProperty(0)
    note_svt = NumericProperty(0)
    note_anglais_ecrit = NumericProperty(0)
    note_anglais_oral = NumericProperty(0)
    note_eps = NumericProperty(0)
    note_facultative = NumericProperty(0)

    def __init__(self, **kwargs):
        super(NotesParCandidat, self).__init__(**kwargs)
        self.load_sample_data()

    def load_sample_data(self):
        # Données exemple
        self.numero_table = "12345"
        self.prenom = "Moussa"
        self.nom = "DIOP"
        self.date_naissance = "01/01/2008"
        self.lieu_naissance = "Dakar"
        
        # Notes exemple
        self.note_compo_franc = 15
        self.note_dictee = 14
        self.note_etude_texte = 16
        self.note_inst_civique = 17
        self.note_hist_geo = 13
        self.note_maths = 18
        self.note_pc_lv2 = 15
        self.note_svt = 16
        self.note_anglais_ecrit = 14
        self.note_anglais_oral = 15
        self.note_eps = 16
        self.note_facultative = 17

class NotesCandidat(App):
    def build(self):
        Builder.load_string('''
#:kivy 2.0.0

<NotesParCandidat>:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # Fond blanc
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: 0.3
        padding: 10
        canvas.before:
            Color:
                rgba: 0.2, 0.5, 0.9, 1  
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'Informations du Candidat'
            font_size: '24sp'
            bold: True
            color: 1, 1, 1, 1  

        GridLayout:
            cols: 2
            spacing: 10
            
            Label:
                text: 'N° Table:'
                color: 1, 1, 1, 1  
            Label:
                text: root.numero_table
                color: 1, 1, 1, 1  
                
            Label:
                text: 'Prénom:'
                color: 1, 1, 1, 1  
            Label:
                text: root.prenom
                color: 1, 1, 1, 1  
                
            Label:
                text: 'Nom:'
                color: 1, 1, 1, 1  
            Label:
                text: root.nom
                color: 1, 1, 1, 1  

    ScrollView:
        size_hint_y: 0.7
        
        GridLayout:
            cols: 3
            spacing: 10
            padding: 10
            size_hint_y: None
            height: self.minimum_height
            row_default_height: '40dp'

            # En-têtes
            Label:
                text: 'Matière'
                bold: True
                size_hint_y: None
                height: '40dp'
                color: 0, 0, 0, 1 
            Label:
                text: 'Note/20'
                bold: True
                size_hint_y: None
                height: '40dp'
                color: 0, 0, 0, 1 
            Label:
                text: 'Coefficient'
                bold: True
                size_hint_y: None
                height: '40dp'
                color: 0, 0, 0, 1 

            # Composition Française
            Label:
                text: 'Composition Française'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_compo_franc)
                color: 0, 0, 0, 1 
            Label:
                text: '2'
                color: 0, 0, 0, 1 

            # Dictée
            Label:
                text: 'Dictée'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_dictee)
                color: 0, 0, 0, 1 
            Label:
                text: '1'
                color: 0, 0, 0, 1 

            # Étude de texte
            Label:
                text: 'Étude de texte'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_etude_texte)
                color: 0, 0, 0, 1 
            Label:
                text: '1'
                color: 0, 0, 0, 1 

            # Instruction Civique
            Label:
                text: 'Instruction Civique'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_inst_civique)
                color: 0, 0, 0, 1 
            Label:
                text: '1'
                color: 0, 0, 0, 1 

            # Histoire-Géographie
            Label:
                text: 'Histoire-Géographie'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_hist_geo)
                color: 0, 0, 0, 1 
            Label:
                text: '2'
                color: 0, 0, 0, 1 

            # Mathématiques
            Label:
                text: 'Mathématiques'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_maths)
                color: 0, 0, 0, 1 
            Label:
                text: '4'
                color: 0, 0, 0, 1 

            # PC/LV2
            Label:
                text: 'PC/LV2'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_pc_lv2)
                color: 0, 0, 0, 1 
            Label:
                text: '2'
                color: 0, 0, 0, 1 

            # SVT
            Label:
                text: 'SVT'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_svt)
                color: 0, 0, 0, 1 
            Label:
                text: '2'
                color: 0, 0, 0, 1 

            # Anglais Écrit
            Label:
                text: 'Anglais Écrit'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_anglais_ecrit)
                color: 0, 0, 0, 1 
            Label:
                text: '2'
                color: 0, 0, 0, 1 

            # Anglais Oral
            Label:
                text: 'Anglais Oral'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_anglais_oral)
                color: 0, 0, 0, 1 
            Label:
                text: '1'
                color: 0, 0, 0, 1 

            # EPS
            Label:
                text: 'EPS'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_eps)
                color: 0, 0, 0, 1 
            Label:
                text: '1'
                color: 0, 0, 0, 1 

            # Épreuve Facultative
            Label:
                text: 'Épreuve Facultative'
                color: 0, 0, 0, 1 
            Label:
                text: str(root.note_facultative)
                color: 0, 0, 0, 1 
            Label:
                text: 'Bonus'
                color: 0, 0, 0, 1 
''')
        return NotesParCandidat()
    
