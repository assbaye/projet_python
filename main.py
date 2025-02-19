from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager






# Ecran de connexion
class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

#Ecran d'ajout de matiere
class MatiereScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

class MainApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MatiereScreen(name='matiere'))
        return sm
    
if __name__ == '__main__':
    MainApp().run()

    