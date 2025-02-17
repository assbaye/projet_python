from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel

# "Dasboard","Candidat","Matiere","Evaluation"
class AccueilView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Dasboard"
        label = MDLabel(text="Page d'Accueil", halign="center")
        self.add_widget(label)

class AproposView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Candidat"
        label = MDLabel(text="À propos de nous", halign="center")
        self.add_widget(label)

class ContactView(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Matiere"
        label = MDLabel(text="Page de Contact", halign="center")
        self.add_widget(label)
