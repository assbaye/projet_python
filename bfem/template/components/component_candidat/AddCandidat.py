from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.screen import MDScreen




class AddCandidat(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(
            MDLabel(
                text=self.name
            )
        )
