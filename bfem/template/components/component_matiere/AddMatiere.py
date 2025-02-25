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
                    on_release:root.addmatiere()   

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
                    on_release:root.addmatiere()  
                                    
"""

Builder.load_string(KV)
class AddMatiere(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addmatiere()

    # def on_kv_post(self,base_widget):
    #     self.addmatiere()
    def addmatiere(self):
        interface_matiere = Matiere()
        matiere = self.ids.nom_matiere.text
        coef = self.ids.coefficient.text
        try:
            if matiere and coef:
                aadd = interface_matiere.add_matiere(matiere,coef)

            print(" bon bon",aadd)
        except Exception as e:
            print("Error",e)
        

        


       