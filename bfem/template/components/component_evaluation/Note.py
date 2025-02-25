from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivy.uix.effectwidget import Rectangle
from kivy.uix.accordion import StringProperty
from kivymd.uix.banner.banner import OneLineListItem
from kivymd.uix.datatables.datatables import MDDropdownMenu
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.metrics import dp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))



from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivymd.uix.banner.banner import MDFlatButton
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivy.uix.filechooser import Screen
from kivy.lang import Builder
from .AddNote import AddNote
from kivymd.app import MDApp
from bfem.database.matiere import Matiere
from .ListeNote import ListNote



KV = """
<Note> :
    MDNavigationLayout:

        MDScreenManager:
            id:screen_manager
            MDScreen:
                MDBoxLayout:
                    orientation:"vertical"
                    padding: ('10dp', '10dp', '10dp', '10dp')
                    # md_bg_color:"#000000"
                   
                      
                    MDBoxLayout:
                        id: box_nav
                        orientation:"horizontal"
                        height: dp(60)
                        size_hint: 1, None
                        pos_hint: {'top': 1,}
                        # md_bg_color:"#000000"
                        spacing: '10dp'
                        padding:(    '10dp', '10dp', '10dp', '10dp')
                        MDBoxLayout:
                            id: navigation
                            orientation:"horizontal"
                            spacing: '10dp'
                            size_hint_x: None
                        Widget:
                            size_hint_x:0.6

                        MDBoxLayout:
                            id: nav_plus
                            orientation:"horizontal"
                            # md_bg_color:"#ffffff"
                        
                            size_hint: None,None
                            height:100
                            
                            # spacing: '10dp'
                            # padding:(    '30dp', '10dp', '10dp', '0dp')
                            MDTextField:
                                id:selected_matiere
                                hint_text:"Matiere"
                                size_hint:[1,None]
                                height: "40dp"
                                readonly: True
                                width:200
                                model:"rectangle"
                                on_focus:if self.focus: root.show_dropdown(self)
                                pos_hint:{"bottom": 1}
            
                        
                       
                    ScreenManager:
                        id:screen_manager_current
                        AddNote:
                            name: "ajouter_des_notes"
                            id:addnote
                        ListNote:
                            name: "liste_des_notes"
                            id: listenote
                
"""


Builder.load_string(KV)

class Note(MDScreen):

    session = StringProperty("Session 1")
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
    


    def set_session(self, session):
        self.session = session
     
        
       


        
       

    def on_kv_post(self, base_widget):
        box_layout = self.ids.navigation
        current_screen = self.ids.screen_manager_current

         # Liste des éléments de navigation
        self.list_navigation = [
            {
                "text": "Ajouter un note",
                "icon": "book-plus",
                "screen": AddNote(name="ajouter des note")
            },
             {
                "text": "Liste des notes",
                "icon": "book-plus",
                "screen": ListNote(name="Liste des notes",id="listenote")
            },  
        ]
        # Ajouter chaque écran dans le ScreenManager
        for nav in self.list_navigation:
            current_screen.add_widget(nav["screen"])

        # Créer les boutons pour chaque élément de navigation
        for nav in self.list_navigation:
            bouton_navigation = MDFlatButton(
                icon=nav["icon"],
                text=nav["text"],
                md_bg_color="#256D94",
                theme_text_color="Custom",
                text_color="#ffffff",
                on_press=lambda instance, screen_manager_content=current_screen: self.switch_navigation(instance, screen_manager_content)
            )
            box_layout.add_widget(bouton_navigation)
        
        
       

    def switch_navigation(self,instance,screen_manager_content=None):
       
        screen_name = instance.text  

        for nav in self.list_navigation:
            if nav["text"] == screen_name:
                screen_manager_content.current = nav["screen"].name
                return     
                
    def open_menu(self,text_field):
        print("IDs disponibles:", self.parent)
        interface_matiere = Matiere()
        menu_items = [
            {"text": matiere, "viewclass": "OneLineListItem", "on_release": lambda x=matiere: self.select_matiere(x)}
            for matiere in interface_matiere.getAll()
        ]
        self.menu = MDDropdownMenu(
            caller=self.ids.selected_matiere,
            items=menu_items,
            width_mult=4
        )
        self.menu.open()

  
    def show_dropdown(self, textfield):
        """Affiche le menu déroulant sous le champ MDTextField."""
        matiere = Matiere()
        if not textfield:  # Vérification si textfield est valide
            print("Erreur: textfield est None")
            return
        
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": mat[1],
                "on_release": lambda x=mat: self.set_matiere(textfield, x[1],x[0]),
            } for mat in matiere.getAll()
        ]
        
        self.menu = MDDropdownMenu(
            caller=textfield,
            items=menu_items,
            width_mult=4,
        )

        if self.menu:
            self.menu.open()

    def set_matiere(self, textfield, value,id):

        if not hasattr(self, 'ids') or 'listenote' not in self.ids:
            print("Erreur: ID 'listenote' non trouvé")
            return
        textfield.text = value
        lstnote = self.ids.listenote
        lstnote.set_matiere(str(id))
        addnote = self.ids.addnote
        addnote.set_matiere(str(id))
        
        if self.menu:
            self.menu.dismiss()

   

    
# class test(MDApp):
#     def build(self):
#         return Note()
    

# test().run()