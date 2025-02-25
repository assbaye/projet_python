from kivymd.uix.banner.banner import MDFlatButton
from kivy.uix.filechooser import error
from kivy.uix.accordion import StringProperty
from kivymd.uix.card.card import MDRelativeLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.backdrop.backdrop import MDFloatLayout
from kivy.uix.accordion import FloatLayout
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from bfem.database.jury import Jury 

KV = """
<ClickableTextField>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        password: True
        icon_left: "key-variant"

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True

<LoginScreen>:
    MDFloatLayout:
        md_bg_color:"#CCEEFF"
        MDBoxLayout:
            id:"main_form"
            pos_hint: {'center_x': 0.5,'center_y': .5}
            md_bg_color:"#ffffff"
            size_hint: [None, None]
            size:[600,400]
            orientation:"vertical"
            radius:18
            padding:20
            spacing:10
            MDBoxLayout:
                id:"header_form"
                orientation:"vertical"
                spacing:2
                pos_hint:{'top': 1}
                size_hint:[1,None]
                MDLabel:
                    text:"Connection Exemen BFEM "
                    bold:True
                    font_size:28
                    halign:"center"
                MDLabel:
                    text:"Gestion des evaluation"
                    # font_size=10,
                    color:"#d9d9d9"
                    halign:"center"
            MDBoxLayout:
                orientation:"vertical"
                spacing:5
                MDTextField:
                    id:telephone
                    hint_text:"Telephone"
                    icon_left:"phone"
                ClickableTextField:
                    id:motdepasse
                    hint_text:"Votre mot de passe"
                MDFillRoundFlatButton:
                    text:"Connecter"
                    md_bg_color:"#ff7300"
                    on_release:root.login()    
"""
Builder.load_string(KV)

class ClickableTextField(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
   
class LoginScreen(MDScreen):
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
    # def on_kv_post(self,base_widget):
    #     # self.login()
      

    def login(self,instance=None):
        print("Bonjour")
        app = MDApp.get_running_app()
        telephone = self.ids.telephone

        motdepasse = self.ids.motdepasse
        
        if not telephone.text:
            telephone.error = True
            telephone.helper_text_mode = "on_error"
            telephone.helper_text = "Veuillez entrer un numéro de téléphone."
            

        if not motdepasse.ids.text_field.text:
            mdp = motdepasse.ids.text_field
            mdp.error = True
            mdp.helper_text_mode = "on_error"
            mdp.helper_text = "Veuillez entrer un mot de passe."
          
        # app.connect("baseapp")  
        # interjury = Jury()
        # connect = interjury.login(telephone.text,motdepasse.text)
        if motdepasse.ids.text_field.text =="1234" and telephone.text == "770000918" :
            app.connect("baseapp")  
        else : 
            telephone.error = True
            telephone.helper_text_mode = "on_error"
            telephone.helper_text = "Veuillez entrer un numéro de téléphone."
            mdp = motdepasse.ids.text_field
            mdp.error = True
            mdp.helper_text_mode = "on_error"
            mdp.helper_text = "Veuillez entrer un mot de passe."
          
            



    



