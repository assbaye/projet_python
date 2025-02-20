from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen



class ListMatiere(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._md_bg_color="#cecece"
        self.add_widget(
            MDLabel(
                text=self.name,
            )
        )