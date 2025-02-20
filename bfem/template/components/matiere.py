from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen



class Matiere(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MDBoxLayout(
         MDLabel(
             text=self.name,
             font_style="H2",
             halign="center",

             shorten=True,
         ),
         padding="12dp",
         pos_hint={'center_x': 0.5, 'center_y': 0.5}
     ))
