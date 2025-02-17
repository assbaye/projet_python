from kivymd.app import MDApp
from kivy.lang import Builder
from views import AccueilView, AproposView, ContactView
from drawer import Drawer

class MainApp(MDApp):

    def build(self):
        # Charger le fichier .kv
        return Builder.load_file("content.kv")

    def on_start(self):
        # Ajouter les vues dans le ScreenManager
        self.root.ids.screen_manager.add_widget(AccueilView())
        self.root.ids.screen_manager.add_widget(AproposView())
        self.root.ids.screen_manager.add_widget(ContactView())

if __name__ == "__main__":
    MainApp().run()
