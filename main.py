from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.lang import Builder
from screens.add_matiere_screen import AddMatiereScreen
from screens.login_screen import LoginScreen
from screens.update_screen_matiere import UpdateMatiereScreen



class ClickableLabel(ButtonBehavior, Label):
    pass


class MainApp(App):
    def build(self):
        Builder.load_file("screen_kv/login.kv")
        Builder.load_file("screen_kv/ajout_matiere.kv")
        Builder.load_file("screen_kv/update_matiere.kv")
        
        
        
        
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(AddMatiereScreen(name='add_matiere'))
        sm.add_widget(UpdateMatiereScreen(name='update_matiere'))
        return sm
    
if __name__ == '__main__':
     MainApp().run()


