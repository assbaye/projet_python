from kivymd.uix.navigationdrawer.navigationdrawer import MDScrollView
from kivymd.uix.datatables import MDDataTable
from kivy.uix.accordion import StringProperty
from kivymd.uix.bottomsheet.bottomsheet import MDLabel
from kivymd.uix.bottomnavigation.bottomnavigation import MDScreen
from kivy.lang import Builder
from bfem.database.anonymous import AnonymatDatabase
from kivy.metrics import dp
from bfem.database.matiere import Matiere


KV = """
<ListAnonymat>
    MDBoxLayout:
        id: contenaire
        
        size_hint:[1,None]
        pos_hint: {'top':1}
        MDLabel:
            text: "Listes des anonymats"
            id:ano_matiere
            halign:"center"
            font_size:28
            bold: True
            pos_hint: {'top': 1}
"""
Builder.load_string(KV)

class ListAnonymat(MDScreen):
    
    id_matiere = StringProperty("Tous")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scroll_view = MDScrollView(
            pos_hint={"top":0.9}
        )
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Anonymats", dp(30)),
                ("Id matiere", dp(30)),
                ("Num Table", dp(30)),
                ("Session", dp(30)),
            ],
            row_data=self.getdata(self.id_matiere),
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.scroll_view.add_widget(self.data_tables)
        self.add_widget(self.scroll_view)
    
    def set_matiere(self, id_matiere):
        matiere = Matiere().get_matiere(id_matiere)
        self.id_matiere = id_matiere
        self.ids.ano_matiere.text = f"Liste des anonymats pour le {matiere[1]}"
        self.update_table()  # Met à jour la table lorsque id_matiere change
    
    def update_table(self):
        # Met à jour les données de la table en fonction de id_matiere
        self.data_tables.row_data = self.getdata(self.id_matiere)
    
    def getdata(self, id_matiere=None):
        interface_anonymous = AnonymatDatabase()
        if id_matiere:
            return interface_anonymous.get_anomonymat_by_matiere(id_matiere)
        return interface_anonymous.getAll()

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
