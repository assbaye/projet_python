from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.utils import get_color_from_hex
from bfem.database.matiere import Matiere

# Définition du style KV pour le composant
Builder.load_string('''
<ListMatiere>:
    BoxLayout:
        orientation: 'vertical'
        spacing: 10
        size_hint: 0.7, 1


        # Zone liste des matières
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 0.9
            canvas.before:
                Color:
                    rgba: get_color_from_hex("#FFFFFF")
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [20, 20, 20, 20]
            
            # En-têtes
            GridLayout:
                cols: 2
                size_hint: 1, None
                height: dp(40)
                padding: dp(10)
                spacing: dp(5)
                
                Label:
                    text: 'Nom de la matière'
                    bold: True
                    font_name: 'bfem/assets/fonts/sen.ttf'
                    color: get_color_from_hex("#000000")
                    font_size: 14
                    size_hint_x: 1
                    text_size: self.size
                    halign: 'center'
                    valign: 'middle'

                Label:
                    text: 'Coefficient'
                    bold: True
                    font_name: 'bfem/assets/fonts/sen.ttf'
                    color: get_color_from_hex("#000000")
                    font_size: 14
                    size_hint_x: 1
                    text_size: self.size
                    halign: 'center'
                    valign: 'middle'

            # Liste des matières
            MatiereList:
                id: matiere_list
                viewclass: 'MatiereItem'
                bar_width: dp(10)
                bar_color: get_color_from_hex("#256D94")
                bar_inactive_color: get_color_from_hex("#CCCCCC")
                effect_cls: "ScrollEffect"
                scroll_type: ['bars', 'content']

                RecycleBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    default_size: None, dp(40)
                    default_size_hint: 1, None
                    spacing: dp(2)
                    padding: dp(10)

<MatiereItem>:
    orientation: 'horizontal'
    size_hint_y: None
    height: dp(40)
    padding: dp(5)
    spacing: dp(5)
    canvas.before:
        Color:
            rgba: 250/255, 250/255, 250/255, 0.6
        Rectangle:
            size: self.size
            pos: self.pos

    Label:
        text: root.nom_matiere
        size_hint_x: 1
        text_size: self.size
        halign: 'center'
        valign: 'middle'
        font_name: 'bfem/assets/fonts/sen.ttf'
        color: get_color_from_hex("#000000")

    Label:
        text: root.coefficient 
        size_hint_x: 1
        text_size: self.size
        halign: 'center'
        valign: 'middle'
        font_name: 'bfem/assets/fonts/sen.ttf'
        color: get_color_from_hex("#000000")
''')

class MatiereList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matiere = Matiere()
        self.refresh_data()
        
    def refresh_data(self):
        self.data = []
        liste_matieres = self.matiere.getAll()
        print(liste_matieres)
        if liste_matieres:
            for matiere in liste_matieres:
                self.data.append({
                    "nom_matiere": matiere[1],
                    "coefficient": str(matiere[2])
                })

class ClickableLabel(ButtonBehavior, Label):
    pass

class MatiereItem(BoxLayout):
    nom_matiere = StringProperty("")
    coefficient = StringProperty("")

class ListMatiere(Screen):
    def on_enter(self):
        if "matiere_list" in self.ids:
            self.ids.matiere_list.refresh_data()
    def go_to_add_matiere(self):
        self.manager.current = 'add_matiere'
