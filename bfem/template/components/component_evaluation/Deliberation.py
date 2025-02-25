from kivy.uix.accordion import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder

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
    session = StringProperty("1")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



