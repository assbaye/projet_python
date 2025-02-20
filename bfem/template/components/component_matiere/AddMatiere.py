from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen







from kivy.lang import Builder


Builder.load_file("bfem/template/components/component_matiere/AddMatiere.kv")
class AddMatiere(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       