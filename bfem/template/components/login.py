from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.backdrop.backdrop import MDFloatLayout
from kivy.uix.accordion import FloatLayout
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp

Kv = """
BoxLayout:
        canvas.before:  
            Color:
                rgba: hex("#CCEEFF")
            Rectangle:
                size: self.size
                pos: self.pos
        orientation: 'vertical'
        padding: 40
        spacing: 10

        Label:
            text: 'Examen BFEM'
            color: hex("#000000")
            font_size: 24
            bold: True
            size_hint: 1, 0.1  

        FloatLayout: #conteneur du formulaire
            orientation: 'vertical'
            canvas.before:  
                Color:
                    rgba: hex("#FFFFFF")
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [20, 20, 20, 20]  
            size_hint: None, None
            size: 300, 400
            pos_hint: {'center_x': 0.5,'center_y': 0.5}  

            Label:
                text: "Connexion"
                color: hex("#FF7300")
                font_size: 18
                bold: True
                size_hint: 0.8, 0.01
                pos_hint: {'center_x': 0.5, 'top': 0.9}
            BoxLayout:
                
                orientation: 'vertical'
                size_hint: 0.8, 0.2
                pos_hint: {'center_x': 0.5, 'top': 0.8}
                padding: 5

                Label: #label pour le champ telephone

                    text: 'Téléphone'
                    color: hex("#000000")
                    opacity: 0.5
                    font_size: 12
                    size_hint: 1, 0.1
                    pos_hint: {'center_x': 0.13}
                TextInput: #champ de saisie pour le telephone
                    id: telephone
                    multiline: False
                    size_hint: 1, 0.1
                    font_size: 16
                    padding: 5, 5

            BoxLayout: #conteneur pour le champ mot de passe
                
                orientation: 'vertical'
                size_hint: 0.8, 0.2
                pos_hint: {'center_x': 0.5, 'top': 0.6}
                padding: 5
                Label: #label pour le champ mot de passe

                    text: 'Mot de passe'
                    color: hex("#000000")
                    opacity: 0.5
                    font_size: 12
                    size_hint: 1, 0.1
                    pos_hint: {'center_x': 0.16}
                TextInput: #champ de saisie pour le mot de passe
                    id: mot_de_passe
                    multiline: False
                    size_hint: 1, 0.1
                    font_size: 16
                    background_color: hex("#FFFFFF")
                    cursor_blink: True
                    padding: 5, 5    
                    password:True
                    # background_color: 211, 211, 211
                    # background_down:211, 211, 211
                   
                   

            BoxLayout: #conteneur pour les boutons
                
                orientation: 'vertical'
                size_hint: 0.8, 0.2
                pos_hint: {'center_x': 0.5, 'top': 0.36}
                spacing:4

                Button: #bouton pour se connecter
                    text: "Se connecter"
                    font_size:16
                    color:hex("#FFFFFF")
                    size_hint:0.98, 0.1
                    pos_hint:{'center_x':0.5}
                    background_color:hex("#256D94")
                    background_down:''
                    background_normal:''

                Label: #label pour le lien d'inscription
                    text: "Pas de compte? S'inscrire"
                    color: hex("#000000")
                    opacity: 0.5
                    font_size: 12
                    size_hint: 1, 0.1
                    pos_hint: {'center_x': 0.5}


"""

class LoginScreen(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            MDFloatLayout(
                MDBoxLayout(
                    MDBoxLayout(
                        MDLabel(
                            text="Connection ",
                           
                            bold=True,
                            halign="center"
                        ),
                        MDLabel(
                            text="Gestion des evaluation",
                            # font_size=10,
                            color="#d9d9d9",
                            halign="center"
                        ),
                      
                        id="header_form",
                        orientation="vertical",
                        spacing=2
                    ),
                    MDBoxLayout(
                        MDTextField(
                            id="telephone",
                            hint_text="Telephone"
                        
                        ),
                         MDTextField(
                             id="motdepasse",
                            hint_text="Mot de passe "
                        ),
                        MDFillRoundFlatButton(
                            text="Connecter",
                            md_bg_color="#ff7300",
                            on_release= lambda instance: self.login(instance) 
                        ),
                        orientation="vertical",
                        spacing=5,

                    ),
                    
                    id="main_form",
                    pos_hint= {'center_x': 0.5,'center_y': .5},
                    md_bg_color="#ffffff",
                    size_hint= [None, None],
                    size=[600,400],
                    orientation="vertical",
                    radius=18,
                    padding=20,
                    spacing=10
                ),
                
                # size=self.size,
                # pos=self.pos,
                # orientation= 'vertical',
                md_bg_color="#CCEEFF",
                # padding=40,
                # spacing=10,
            )
        )

    def login(self,instance=None):
        app = MDApp.get_running_app()  # Récupère l'instance de l'application
        app.connect("baseapp")  # Change d'écran



    



