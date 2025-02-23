from kivy.uix.accordion import StringProperty
from kivymd.uix.behaviors.toggle_behavior import MDRectangleFlatIconButton
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp
from bfem.database.anonymous import AnonymatDatabase
from bfem.database.matiere import Matiere

# color:
# bleu clair =>CCEEFF
# grid1 =>D9D9D9
# bleu fonce => 256D94
# noir =>000000
# blanc => FFFFFF
# vert => 44B3B1
# orange => FF7300
KV = """
<AddNote>:
    MDFloatLayout:
        
        MDBoxLayout:
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            size_hint: None, None
            size: '500dp','300'
            orientation:"vertical"
            # md_bg_color:"#CCEEFF"
            line_color:"#cecece"
            radius:20
            spacing: '10dp'
            padding:[70,10]
            elevation:3
            MDBoxLayout:
                MDLabel:
                    id:matiere
                    # text: 'Ajouter des notes'
                    halign:"center"
                    font_size:28
                    bold: True
            MDBoxLayout:
                spacing: '20dp'
                MDTextField:
                    id:"anonymat"
                    hint_text:"Anonymat"
                MDTextField:
                    id:"note"
                    hint_text:"Note"
            MDBoxLayout:
                pos_hint: {'center_x': 0.7}
                spacing: '20dp'
                MDRectangleFlatIconButton:
                    text: 'Sauvegarder'
                    theme_text_style:'Custom',
                    text_color:"#ffffff"
                    md_bg_color:"#FF7300"
                    line_color:"#ffffff"
                MDRectangleFlatIconButton:
                    text: 'Sauvegarder et continuer'
                    theme_text_style:'Custom',
                    text_color:"#ffffff"
                    md_bg_color:"#44B3B1"
                    line_color:"#ffffff"

    
"""

Builder.load_string(KV)

class AddNote(MDScreen):
    matiere = StringProperty("")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

  
    def set_matiere(self,matiere_id):
        matiere = Matiere().get_matiere(matiere_id)

        self.matiere = matiere_id
        self.ids.matiere.text ="Ajouter des notes de  "+ matiere[1]







# class test(MDApp):

#     def build(self):
#         return AddNote()
    

# test().run()