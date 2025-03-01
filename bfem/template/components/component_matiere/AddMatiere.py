from kivymd.uix.datatables.datatables import MDDropdownMenu
from kivy.uix.filechooser import error
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivy.lang import Builder
from bfem.database.matiere import Matiere

KV ="""

#Ecran pour matiere

#: import hex kivy.utils.get_color_from_hex
<AddMatiere>:
           #Ajout Matiere Principal 
    BoxLayout:
        orientation: 'vertical'
        spacing: 10
        
        size_hint: 1,1
        FloatLayout:
            padding: 40
            spacing: 10
            size_hint: 1, 1
            canvas.before:  
                Color:
                    rgba: hex("#FFFFFF")
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [20, 20, 20, 20]

            BoxLayout:
                canvas:
                    Color:
                        rgba: hex("#D9D9D9")
                    Line:
                        width: 1
                        rounded_rectangle: self.x, self.y, self.width, self.height, 20

                orientation: 'horizontal'
                padding: 20
                spacing: 10  
                size_hint: 0.95, 0.2
                pos_hint: {'center_x': 0.5, 'top': 0.8}

                    
                BoxLayout:
                   
                    orientation: 'vertical'
                    size_hint: 0.33, 1  
                    padding: 5
                    MDTextField:
                        id: nom_matiere
                        hint_text: "Nom de la Matiere"

                BoxLayout:
                       
                    orientation: 'vertical'
                    size_hint: 0.33, 1
                    padding: 5

                    MDTextField:
                        hint_text: "Coefficient"
                        id:coefficient
                BoxLayout:
                       
                    orientation: 'vertical'
                    size_hint: 0.33, 1
                    padding: 5

                    MDTextField:
                        hint_text: "C'est du bonus"
                        text:"Faux"
                        id:bonus
                        on_focus:if self.focus: root.open_menu(self,"bonus") 
                  
            BoxLayout:
                orientation: 'horizontal'
                spacing:5
                padding:10
                size_hint: 0.7, 0.3
                pos_hint: {'x': 0.3, 'y': 0.4}

                Button:
                    id: save
                    text: "Sauvegarder"
                    font_size: 16
                    color: hex("#FFFFFF")
                    size_hint: 0.3, 0.2
                    pos_hint: {'center_x': 0.5}
                    background_color: hex("#ff7300")
                    background_down:''
                    background_normal:''      
                    on_release:root.addmatiere("liste")   

                Button:
                    id: save_continue
                    text: "Sauvegarder et Continuer"
                    font_size: 16
                    color: hex("#ffffff")
                    size_hint: 0.7, 0.2
                    pos_hint: {'center_x': 0.5}
                    background_color: hex("#256D94")
                    background_down:'hex("#256D99")'
                    background_normal:''
                    on_release:root.addmatiere("continuer")  
                                    
"""

Builder.load_string(KV)
class AddMatiere(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def on_kv_post(self,*args):
        self.menus = {
            "bonus": MDDropdownMenu(
                caller=self.ids.bonus,
                items=[
                    {
                        "text": "Vrai",
                        "on_release": lambda x="Vrai": self.set_item("bonus", x),
                    },
                    {
                        "text": "Faux",
                        "on_release": lambda x="Faux": self.set_item("bonus", x),
                    },
                    {
                        "text": "Malus",
                        "on_release": lambda x="Malus": self.set_item("bonus", x),
                    },
                ],
                width_mult=3,
            ),
        }
       
    
   
    def open_menu(self, caller, menu_type):
     
       if menu_type in self.menus:
        self.menus[menu_type].caller = caller  # Associez le calle
        self.menus[menu_type].open()  # Ouvrez le menu
       else:
        print(f"Erreur : le menu '{menu_type}' n'existe pas.")

    def set_item(self, item_type, value):
        """Définit la valeur sélectionnée dans le menu"""
        setattr(self, item_type, value)
        self.ids[item_type].text = value
        self.menus[item_type].dismiss()

    def addmatiere(self,action):
        interface_matiere = Matiere()
        matiere = self.ids.nom_matiere
        coef = self.ids.coefficient
        bonus = self.ids.bonus

        valited = True
        for field in ["nom_matiere", "coefficient","bonus"]:
            if getattr(self.ids, field).text == "":
                field = getattr(self.ids,field)
                field.error = True
                field.helper_text_mode = "on_error"
                field.helper_text = "Veuillez Remplir le champs"
                valited = False
        if valited == False : return

        if 0> int(coef.text)>=5:
            coef.error =True
            coef.helper_text_mode = "on_error"
            coef.helper_text = "Le coefficeint doit etre compris entre 0 et 4"
            valited = False
            return 
        
        bonus_valeur = 1 if bonus.text == "Vrai" else 2 if bonus.text == "Malus" else 0

        if action == "continuer":
            interface_matiere.add_matiere(matiere.text,coef.text,bonus_valeur)
            coef.text = " "
            matiere.text = " "
            liste_screen = self.manager.get_screen("Liste_matiere")
            liste_screen.update_table()

        else:
            liste_screen = self.manager.get_screen("Liste_matiere")
            liste_screen.update_table()
            self.manager.current="Liste_matiere"

        

        


       