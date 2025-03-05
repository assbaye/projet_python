from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

KV = """
<StatistiquesScreen>:
    name: "statistiques"
    BoxLayout:
        orientation: 'vertical'

        MDBoxLayout:
            spacing: 10
            padding: [10, 10, 10, 10]
            adaptive_height: True
            md_bg_color:   "#FF7300"
            MDLabel:
                text: 'Statistiques après délibérations'
                color: 1 , 1,1,1
                size_hint: 1, None
                halign: "center"
                bold: True

        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(10)
            spacing: dp(10)

            MDCard:
                size_hint: None, None
                size: "350dp", "100dp"
                padding: "10dp"
                md_bg_color: [0.9, 0.95, 1, 1]
                MDLabel:
                    id: total_candidats
                    text: "Total candidats : 200"
                    halign: "center"
                    bold: True

            MDCard:
                size_hint: None, None
                size: "350dp", "100dp"
                padding: "10dp"
                md_bg_color: [0.8, 1, 0.8, 1]
                MDLabel:
                    id: admis
                    text: "Admis : 120"
                    halign: "center"
                    bold: True

            MDCard:
                size_hint: None, None
                size: "350dp", "100dp"
                padding: "10dp"
                md_bg_color: [1, 0.8, 0.8, 1]
                MDLabel:
                    id: ajournes
                    text: "Ajournés : 80"
                    halign: "center"
                    bold: True

            MDCard:
                size_hint: None, None
                size: "350dp", "100dp"
                padding: "10dp"
                md_bg_color: [0.8, 0.8, 1, 1]
                MDLabel:
                    id: taux_reussite
                    text: "Taux de réussite : 60%"
                    halign: "center"
                    bold: True

        MDRaisedButton:
            text: "Retour"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = "liste_candidats"

"""
Builder.load_string(KV)

class StatistiquesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_pie_chart()

    def create_pie_chart(self):
        admis = 120
        ajournes = 40
        repeches = 40
        labels = ['Admis', 'Ajournés','repeches ']
        sizes = [admis, ajournes,repeches ]
        colors = ['#4CAF50', '#F44336','#F88446']
        
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        pie_chart = FigureCanvasKivyAgg(fig)
        self.add_widget(pie_chart)

class MainApp(MDApp):
    def build(self):
        return StatistiquesScreen()

if __name__ == "__main__":
    MainApp().run()
