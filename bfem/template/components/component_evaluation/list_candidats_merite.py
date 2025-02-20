from kivy.uix.screenmanager import Screen
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from bfem.database.candidat import Candidat

class StudentList(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.candidat = Candidat()
        self.refresh_data()
        
        #Recuperation des candidats pour test
        
    def refresh_data(self):
        liste_candidats = self.candidat.getAll()
        print(self.candidat.getAll())
        print(liste_candidats)
        self.data = []
        for candidat in liste_candidats:
            self.data.append({
                "prenom": candidat[1],
                "nom": candidat[2],
                "sexe": candidat[5],
                "date_naissance": candidat[3],
                "etablissement": candidat[9],
                # "moyenne": str(candidat[10])
            })
        self.candidat.print_to_pdf()
        

class StudentItem(BoxLayout):
    prenom = StringProperty("")
    nom = StringProperty("")
    sexe = StringProperty("")
    date_naissance = StringProperty("")
    etablissement = StringProperty("")
    moyenne = StringProperty("")

class ListeMeriteScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def on_enter(self, *args):
        self.ids.student_list.refresh_data()  # This method is called every time the screen becomes active