from kivy.config import Config
# Config.set('graphics','fullscreen','auto')


from kivy.lang import Builder

from kivymd.app import MDApp

    

class MyApp(MDApp):

    def build(self):

        return Builder.load_file("my_app.kv")
    

MyApp().run()