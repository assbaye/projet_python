from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from bfem.template.MyApp import MyApp





# Ecran de connexion
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#Ecran d'ajout de matiere
class MatiereScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class MainApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MyApp())
        # sm.add_widget(LoginScreen(name='login'))
        # sm.add_widget(MatiereScreen(name='matiere'))
        return sm
    
if __name__ == '__main__':
    MainApp().run()

    