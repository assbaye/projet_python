from kivy.uix.screenmanager import Screen
from screens.login_screen import LoginScreen
from bfem.database.jury import Jury
from bfem.database.matiere import Matiere
from kivy.uix.label import Label
from kivy.uix.popup import Popup





#Ecran d'ajout de matiere

class AddMatiereScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jury = Jury()
        self.matiere = Matiere()
        


        
        
    # def info_jury(self):
    #     admin = None
    #     infos_admin = []
    #     # if LoginScreen().login_jury() is not None:
    #     #     admin = LoginScreen().login_jury()
    #     #     infos_admin = self.jury.get_jury(admin)
    #     #     print(infos_admin)
    #     print(LoginScreen().login_jury())
    def open_popup(self,message):
        content = Label(text=message)
        popup = Popup(title="Erreur", content=content, size_hint=(None, None), size=(300, 200),background_color=(1,0,0,1))
        popup.open()
    
    def add_matieres(self):
        nom_matiere = self.ids.nom_matiere.text.strip()
        coef_text = self.ids.coef_matiere.text.strip()

        # Vérification des champs
        if not nom_matiere:
            self.open_popup("Le nom de la matière est requis !")
            return

        try:
            coef = int(coef_text)
            if coef < 1:
                self.open_popup("Le coefficient doit être supérieur ou égal à 1 !")
                return
        except ValueError:
            self.open_popup("Le coefficient doit être un nombre valide !")
            return

        # Ajout de la matière dans la base de données
        self.matiere.add_matiere(nom_matiere, coef)
        print(self.matiere.getAll())

        # Réinitialiser les champs après ajout
        self.ids.nom_matiere.text = ""
        self.ids.coef_matiere.text = ""

            
    