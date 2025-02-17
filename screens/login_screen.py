
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from bfem.database.jury import Jury


# Ecran de connexion
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jury = Jury()
        
    def open_popup(self,message):
        content = Label(text=message)
        popup = Popup(title="Erreur", content=content, size_hint=(None, None), size=(300, 200),background_color=(1,0,0,1))
        popup.open()

    def login_jury(self):
        telephone = self.ids.telephone.text
        mot_de_passe = self.ids.mot_de_passe.text
        if self.jury.login(telephone,mot_de_passe):
            return self.jury.login(telephone,mot_de_passe)
        else:
            return None
            
            
    def do_login_jury(self):
        if self.login_jury() is not None:
            self.manager.current = 'add_matiere'
        else:
            self.open_popup("Telephone ou mot de passe incorrect")
            
        