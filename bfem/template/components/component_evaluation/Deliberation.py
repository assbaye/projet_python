from kivymd.uix.datatables import MDDataTable
from kivymd.uix.navigationdrawer.navigationdrawer import MDScrollView
from kivy.uix.accordion import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp


from bfem.database.candidat import Candidat
from bfem.database.anonymous import AnonymatDatabase
from bfem.database.matiere import Matiere
from bfem.database.livret_scolaire import LivretScolaire
from bfem.database.examen import Examen


KV ="""
<ListDeliberation>:
   
    MDBoxLayout:
        id: contenaire
        
        size_hint:[1,None]
        pos_hint: {'top':1}
        MDLabel:
            text:"Bonjour "
            id:head
            # text: 'Ajouter des notes'
            halign:"center"
            font_size:28
            bold: True
            pos_hint: {'top': 1}


"""
Builder.load_string(KV)

class ListDeliberation(MDScreen):
     
    session = StringProperty("Session 1")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    
   
    def set_session(self, session):
        self.session = session
      