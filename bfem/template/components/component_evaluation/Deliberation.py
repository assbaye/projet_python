from kivymd.uix.datatables import MDDataTable
from kivymd.uix.navigationdrawer.navigationdrawer import MDScrollView
from kivy.uix.accordion import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))


from bfem.database.candidat import Candidat
from bfem.database.anonymous import AnonymatDatabase
from bfem.database.matiere import Matiere
from bfem.database.livret_scolaire import LivretScolaire
from bfem.database.examen import Examen


KV ="""
<ListDeliberation>:
   
    MDBoxLayout:
        id: contenaire
        size_hint:[1,None]
        height: dp(3)
        pos_hint: {'top':1}
        MDLabel:
            text:"Liste Deliberation pour la "+ self.session
            id:head
            # text: 'Ajouter des notes'
            halign:"center"
            font_size:28
            bold: True
            pos_hint: {'top': 1}


"""
Builder.load_string(KV)

class ListDeliberation(MDScreen):
     
    session = StringProperty("Session 1")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scroll_view = MDScrollView(
            pos_hint={"top":0.9}
        )
        self.data_tables = MDDataTable(
            
            use_pagination=True,
            check=True,
            column_data=self.getdata()[0],
            row_data=self.getdata()[1],
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.scroll_view.add_widget(self.data_tables)
        self.add_widget(self.scroll_view)
    
   
    def set_session(self, session):
        self.session = session

    def getdata(self):
        col = [
             ("no",dp(30)),
            ("prenom",dp(40)),
            ("Nom",dp(30)),
            ("Date de naissance",dp(30)),
            ("Lieu de naissance", dp(30))
            ]
        livret = [
             ("Tentative",dp(20)),
            ("Moyenne 6",dp(20)),
            ("Moyenne 5",dp(20)),
            ("Moyenne 4",dp(20)),
            ("Moyenne 3",dp(20)),

         ]
        matiere = [mat[1] for mat in Matiere().getAll()]
        matieref =[]
        for matf in matiere:
            tup = (str(matf), dp(25))
            matieref.append(tup)
        last = [
                ("total",dp(20)),
                ("Status",dp(20))
        ]
        col +=livret
        col +=matieref
        col +=last
       
        Rows =[]
        for candidat  in Candidat().get_all_candidate():

            row = [
                str(candidat[0]),
                candidat[1],
                candidat[2],
                str(candidat[3]),
                candidat[4],
            ]
             
            livret = LivretScolaire().get_livretscolaire(candidat[0])
            if livret:
                row.extend([
                    str(livret[0]),
                    str(livret[1]),
                    str(livret[2]),
                    str(livret[3]),
                    str(livret[4]),
                ])
            else:
                # Si le livret est absent, remplir avec des espaces vides
                row.extend([" "] * 5)
            notes = Examen().get_notes_by_canidate(candidat[0], self.session)
            notes_dict ={
                str(note[0]): (
                    str(note[1]) 
                ) 
                for note in notes
            }
        
            for matiere in Matiere().getAll():
                
                row.append(notes_dict.get(matiere[1], "  "))

            total = (Examen().sum(candidat[0],self.session))[0][0]

            row.append(str(0) if not total else str(self.Somme(notes)))
            
            total = 0 if not total else total

            if self.session == "Session 1":
                row.append(
                    "Admis" if total > 180 else "Échoué" if total < 153 else "Second tour" 
                )
            else:
                row.append(
                    "Admis" if 76<=total else "Echoue"
                )

            
            Rows.append(row)

           

        return [col,Rows] 
    
    def Somme(self,notes):

        somme = 0
        for note in notes: 
            note_value = note[1]
            matiere = note[0]
            bonus_flag = note[2] 
            coef = note[3] 

           # malus
            if bonus_flag == 2: 
                note = 0 if note_value <= 10 else note_value - 10
                somme += note
            elif bonus_flag == 1: # bonus 
                note = (note_value - 10) if note_value > 10 else (10 -note_value)
                somme +=note
            else:
                somme += note_value*coef
        
        
        return somme
    
    
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

        

class Test(MDApp):
    def build(self):
        return ListDeliberation()

# Test().run()

# print(Candidat().get_all_candidate())