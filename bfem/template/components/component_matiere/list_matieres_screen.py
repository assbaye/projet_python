from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from bfem.database.matiere import Matiere

class MatiereList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.matiere = Matiere()
        self.refresh_data()
    
    def refresh_data(self):
        self.data = []
        liste_matieres = self.matiere.getAll()
        for matiere in liste_matieres:
            self.data.append({
                "nom_matiere": matiere[1], 
                "coefficient": str(matiere[2])
            })

class MatiereItem(BoxLayout):
    nom_matiere = StringProperty("")
    coefficient = StringProperty("")

class ListMatiereScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enter(self):
        # Cette méthode est appelée chaque fois que l'écran devient actif
        self.ids.matiere_list.refresh_data()  