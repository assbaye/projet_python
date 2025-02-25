from kivymd.uix.navigationdrawer.navigationdrawer import MDScrollView
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivy.uix.accordion import StringProperty
from kivy.metrics import dp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))


from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
from bfem.database.matiere import Matiere
from bfem.database.anonymous import AnonymatDatabase
from kivy.clock import Clock
from kivy.lang import Builder

KV="""
<ListeMatiere>:
    MDBoxLayout:
        id: contenaire
        
        size_hint:[1,None]
        pos_hint: {'top':1}
        MDLabel:
            text: "Liste des matieres"
            id:l_matiere
            # text: 'Ajouter des notes'
            halign:"center"
            font_size:28
            bold: True
            pos_hint: {'top': 1}
     
"""
Builder.load_string(KV)

class ListeMatiere(MDScreen):

    id_matiere = StringProperty("Tous")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        scroll_view = MDScrollView(
            pos_hint={"top":0.9}
        )
        data_tables = MDDataTable(
            
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Nom", dp(60)),
                ("Coefficient", dp(40)),
               
            ],
            row_data=self.getdata(),
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        data_tables.bind(on_row_press=self.on_row_press)
        data_tables.bind(on_check_press=self.on_check_press)
        scroll_view.add_widget(data_tables)
        self.add_widget(scroll_view)
        # self.set_matiere(18)
    
   
    
    def getdata(self):

       return Matiere().getAll() 
       

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

  
    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1]),
                    ]
                ),
            )
        )

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))



