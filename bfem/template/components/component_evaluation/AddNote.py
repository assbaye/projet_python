from kivy.uix.accordion import StringProperty
from kivymd.uix.behaviors.toggle_behavior import MDRectangleFlatIconButton
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp
from bfem.database.anonymous import AnonymatDatabase
from bfem.database.matiere import Matiere
from bfem.database.examen import Examen

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
                id: mssg
                orientation:"vertical"
                MDLabel:
                    id:matiere
                    # text: 'Ajouter des notes'
                    halign:"center"
                    font_size:28
                    bold: True
            MDBoxLayout:
                spacing: '20dp'
                MDTextField:
                    id:anonymat
                    hint_text:"Anonymat"
                MDTextField:
                    id:note
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
                    on_release: root.SaveNote('liste')
                MDRectangleFlatIconButton:

                    text: 'Sauvegarder et continuer'
                    theme_text_style:'Custom',
                    text_color:"#ffffff"
                    md_bg_color:"#44B3B1"
                    line_color:"#ffffff"
                    on_release: root.SaveNote('continuer')

    
"""

Builder.load_string(KV)

class AddNote(MDScreen):
    matiere = StringProperty("")
    session = StringProperty("Session 1")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

  
    def set_matiere(self,matiere_id):
        matiere = Matiere().get_matiere(matiere_id)
        self.matiere = matiere_id
        self.ids.matiere.text ="Ajouter des notes de  "+ matiere[1]


    def verifie_anonymat(self,anonymat):
       return False if not AnonymatDatabase().verifie_anonymat(self.matiere,self.session) else True
    
    def SaveNote(self,action):
        anonymat = self.ids.anonymat
        note = self.ids.note

        valited = True

        for field in ["anonymat", "note"]:
            if getattr(self.ids, field).text == "":
                field = getattr(self.ids,field)
                field.error = True
                field.helper_text_mode = "on_error"
                field.helper_text = "Veuillez Remplir le champs"
                valited = False

        if  valited == False : return 
        if not AnonymatDatabase().verifie_anonymat(self.matiere,anonymat.text,self.session) :
            field = getattr(self.ids,"anonymat")
            field.error = True
            field.helper_text_mode = "on_error"
            field.helper_text = "L'anonymat est incorrect"
            valited = False
            return 
        if not Examen().get_note(self.matiere) :
            field = getattr(self.ids,"anonymat")
            field.error = True
            field.helper_text_mode = "on_error"
            field.helper_text = "L'anonymat a deja une note"
            valited = False
            return 
        
        note_value = int(getattr(self.ids, "note").text)

        if not (0 <= note_value <= 20):
            field = getattr(self.ids, "note")
            field.error = True
            field.helper_text_mode = "on_error"
            field.helper_text = "Note doit être comprise entre 0 et 20"

            return False
        
        state =Examen().add_note(note.text,anonymat.text)
        if state == True:
            self.ids.mssg.add_widget(
                MDLabel(
                    text="Note Enregistrer",
                    color="#44B3B1",
                    halign="center"
                )
            )
        else :
              self.ids.mssg.add_widget(
                MDLabel(
                    text="Error",
                    color="#44B3B1",
                    halign="center"
                )
            )
        if action == "continuer":
            
            liste_screen = self.manager.get_screen("liste_des_notes")
            liste_screen.getdata()
            for field in ["anonymat", "note"]: 
                getattr(self.ids, field).text =" "
        
        else:   
             self.manager.current = "liste_des_notes"






        
            








# class test(MDApp):

#     def build(self):
#         return AddNote()
    

# test().run()