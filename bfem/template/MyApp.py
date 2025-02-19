from kivymd.uix.button import MDRaisedButton
from kivymd.uix.navigationdrawer import MDNavigationDrawerHeader
from kivymd.uix.banner.banner import MDFlatButton
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivymd.uix.navigationrail import MDNavigationRailFabButton
from kivymd.uix.navigationrail import MDNavigationRail
from kivymd.uix.navigationdrawer import MDNavigationDrawerMenu
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.navigationrail import MDNavigationRailItem
from kivymd.uix.navigationrail import MDNavigationRailMenuButton
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.bottomsheet.bottomsheet import MDIconButton
from kivymd.uix.behaviors.toggle_behavior import MDFillRoundFlatIconButton
from kivy.clock import Clock
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout

from components.candidats import Candidat
from components.matiere import Matiere


# color:
# bleu clair =>CCEEFF
# grid1 =>D9D9D9
# bleu fonce => 256D94
# noir =>000000
# blanc => FFFFFF
# vert => 44B3B1
# orange => FF7300



class DramerClickableItem(MDNavigationDrawerItem):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.focus_color ="#256D94"
        self.unfocus_color =self.theme_cls.bg_light
        self.selected_color="#cceeff"
        self.radius =20
       

class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.paddding = "16dp"
        # self.elevation=1
        # self.shadow_radius = 2
        # self.shadow_softness = 1
        self.height = dp(70)
    
        Clock.schedule_once(self.set_spacing)
    
    def set_spacing(self,interval):
        self.ids.box.spacing="12dp"
    
    def set_raduis(self,*args):
        if self.rounded_button:
            self._raduis =self.raduis = self.height/4



class MyApp(MDApp):



    def build(self):

        # self.theme_cls.material_style ="M3"
        # self.theme_cls.theme_style = "Light"
        
        # self.theme_cls.primary_palette = "Blue" 

        
         
        return MDScreenManager(

                MDScreen(
                    MDLabel(
                        text="Bonjour",
                        pos_hint= {'center_x': 0.5,'center_y': 0.5},
                    ),
                    MDRaisedButton(
                        text="Connect",
                        on_press=lambda instance: self.connect("baseapp")
                    ),
                    

                    id="login",
                    name="login",
                    ),
             MDScreen(
                 MDNavigationLayout(
                    MDScreenManager(
                    
                    MDScreen(
                        MDBoxLayout(
                            MDBoxLayout(
                                MDLabel(
                                    text= "Examen BFEM",
                                    font_style="H6",
                                    bold=True,
                                    adaptive_height=True,
                                    pos_hint= {'center_y': 0.6},
                                    

                                ),
                                adaptive_height = True,
                                md_bg_color = "#CCEEFF",
                                padding="12dp",
                            ),
                            MDBoxLayout(
                                MDNavigationRail(
                                    
                                MDNavigationRailMenuButton(
                                    on_release =self.open_nav_drawer,
                                ),

                               
                                id="navigation_rail",
                                md_bg_color="#cceeff",
                                selected_color_background="#256D94",
                                ripple_color_item="#256D94",
                                anchor="center",
                                icon_color_item_normal="#256D94",
                                icon_color_item_active="#ffffff"
                               
                               
                            ),

                            MDScreenManager(
                                id="screen_manager_content",
                            ),
                            id="root_box",
                            ),
                            id="box_rail",
                         orientation= 'vertical',
                        ),
                      id="box",  
                    ),
                    id="screen",
                ),
                id="screen_manager",
            ),
                MDNavigationDrawer(

                    MDNavigationDrawerMenu(
                    #  MDNavigationDrawerHeader(
                    #      title="Examen BFEM",
                    #      text="Gestion des examen",
                    #      spacing=dp(4),
                    #      padding=["12dp",0,0,"56dp"],
                         
                    #  ),
                   
                    MDBoxLayout(
                        MDIconButton(
                            icon="Menu",
                        ),
                        ExtendedButton(
                            text="Examen BFEM",
                            icon="gamma",
                            md_bg_color= "#256D94",
                       
                            
                        
                            
                        ),
                        
                        orientation="vertical",
                        adaptive_height=True,
                        spacing="2dp",
                        padding=("3dp",0,0,"12dp"),

                    ),
              
                    id="navigation",
                    
                    
                ),
                
             
                id="nav_drawer",
                radius=(0,10,10,0),
                
               
                width="150dp",
                
               

            ),
                
                id="base",
                name="baseapp"
            ),
            id="systeme_root_manager"

        )
    
    def switch_screen(self,*args,screen_manager_content=None):
        """
        On l'appel si on veut changer d'ecran
        """
        instance_navigation_rail, instance_navigation_rail_item = args

        for route in self.routers:
            if route["icon"] == instance_navigation_rail_item.icon:
                screen_manager_content.current = route["screen"].name
                return
      
  
    def switch_screen_drawer(self, instance_navigation_drawer_item, screen_manager_content):
   
    # Chercher la route correspondante en comparant les icônes
        for route in self.routers:
            if route["icon"] == instance_navigation_drawer_item.icon:  # Vérifie l'icône
                screen_manager_content.current = route["screen"].name
                self.root.ids.base.ids.nav_drawer.set_state("close")
                return

    def open_nav_drawer(self,*args):
        self.root.ids.base.ids.nav_drawer.set_state("open")
    
    def connect(self,screen):
     
        screen_manager = self.root
        if screen_manager:
            screen_manager.current = screen
        
    def on_start(self):
        
        
        '''
        Creates application scrrens.

        '''

        self.routers = [
            {
                "text": "Candidat",
                "icon": "account-group",
                "screen": Candidat(name="candidat")
            },
             {
                "text": "Matiere",
                "icon": "book-open",
                "screen":Matiere(name="matiere")
            },
             {
                "text": "Evaluation",
                "icon": "lightning-bolt",
                "screen":Matiere(name="Evaluation")
            }
        ]

        screen_manager = self.root.ids.base.ids.screen_manager

        root_box = screen_manager.ids.screen.ids.box.ids.box_rail.ids.root_box
        
        navigation_rail =root_box.ids.navigation_rail

        navigation_dramer = self.root.ids.base.ids.nav_drawer.ids.navigation

        
        for route in self.routers:
            item_rail = MDNavigationRailItem(
                                    icon=route["icon"],
                                )
            item_drawer = DramerClickableItem(
                text=route["text"],
                icon=route["icon"]
            )
            navigation_rail.add_widget(item_rail)
            item_drawer.bind(on_release=lambda instance: self.switch_screen_drawer(instance, screen_manager_content))
            navigation_dramer.add_widget(item_drawer)
        disconnect =  DramerClickableItem(
                                    text="Alioune Ndiaye",
                                    icon="logout"
                                )
        disconnect.bind(on_release=lambda instance: self.connect("login"))

        navigation_dramer.add_widget(disconnect)    
        
        
        screen_manager_content = root_box.ids.screen_manager_content

        navigation_rail_items = navigation_rail.get_items()[:]
        

        navigation_rail_items.reverse()
        navigation_rail.bind(
            on_item_release=lambda *args: self.switch_screen(
                *args, screen_manager_content= screen_manager_content
            )
        )

        for route in self.routers:
            name_screen = route["screen"]

            screen_manager_content.add_widget(
                route["screen"]
            )



          



MyApp().run()