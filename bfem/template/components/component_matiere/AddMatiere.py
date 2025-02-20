from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen



class AddMatiere(MDScreen):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(
            MDLabel(
                text=self.name,
            )
        )