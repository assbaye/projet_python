from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.lang import Builder
from screens.add_matiere_screen import AddMatiereScreen
from screens.login_screen import LoginScreen
from screens.update_screen_matiere import UpdateMatiereScreen
from screens.list_candidats_merite import ListeMeriteScreen
from screens.list_matieres_screen import ListMatiereScreen



class ClickableLabel(ButtonBehavior, Label):
    pass


class MainApp(App):
    def build(self):
        Builder.load_file("bfem/template/screen_kv/login.kv")
        Builder.load_file("bfem/template/screen_kv/ajout_matiere.kv")
        Builder.load_file("bfem/template/screen_kv/update_matiere.kv")
        Builder.load_file("bfem/template/screen_kv/list_candidats_merite.kv")
        Builder.load_file("bfem/template/screen_kv/liste_matiere.kv")
        
        
        
        
        sm = ScreenManager()

        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MatiereScreen(name='matiere'))

        # sm.add_widget(LoginScreen(name='login'))
        # sm.add_widget(ListMatiereScreen(name='liste_matiere'))
        # sm.add_widget(AddMatiereScreen(name='add_matiere'))
        # # sm.add_widget(UpdateMatiereScreen(name='update_matiere'))
        sm.add_widget(ListeMeriteScreen(name='liste_merite'))

        return sm
    
if __name__ == '__main__':
     MainApp().run()


