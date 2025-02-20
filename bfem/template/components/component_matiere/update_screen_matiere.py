from kivy.uix.screenmanager import Screen
from screens.login_screen import LoginScreen
from bfem.database.jury import Jury
from bfem.database.matiere import Matiere
from kivy.uix.label import Label
from kivy.uix.popup import Popup





#Ecran d'ajout de matiere

class UpdateMatiereScreen(Screen):
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
    
    def update_matieres(self):
        try:
            matiere_id = int(self.ids.matiere_id.text.strip()) 
        except ValueError:
            self.open_popup("L'ID de la matière doit valide !")
            return

        nom_matiere = self.ids.nom_matiere.text.strip()
        coef_text = self.ids.coef_matiere.text.strip()

        # Récupération des IDs de matières existantes
        ids_matiers = [id[0] for id in self.matiere.getIds()]  

        # Vérifier si l'ID de la matière existe
        if matiere_id not in ids_matiers:
            self.open_popup("Matière non trouvée !")
            return

        # Vérifier le nom de la matière
        if not nom_matiere:
            self.open_popup("Le nom de la matière est requis !")
            return

        # Vérifier le coefficient
        try:
            coef = int(coef_text)
            if coef < 1:
                self.open_popup("Le coefficient 0 imposible!")
                return
        except ValueError:
            self.open_popup("Le coefficient doit être valide !")
            return

        # Mise à jour de la matière
        self.matiere.update_matiere(matiere_id, nom_matiere, coef)
        self.open_popup("Matière modifiée avec succès ✅")

        # Afficher toutes les matières mises à jour
        print(self.matiere.getAll())


            # Réinitialiser les champs après ajout
        self.ids.matiere_id.text= ""
        self.ids.nom_matiere.text = ""
        self.ids.coef_matiere.text = ""

                
        