from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
import os
from datetime import datetime

class ReleveNotesBFEM:
    def __init__(self):
        self.styles = getSampleStyleSheet()
        
    def calculer_points_premier_tour(self, notes):
        # Coefficients du premier tour
        coefficients = {
            'compo_franc': 2,  # Composition Française
            'dictee': 1,       # Dictée
            'etude_texte': 1,  # Étude de texte
            'inst_civique': 1, # Instruction Civique
            'hist_geo': 2,     # Histoire-Géographie
            'maths': 4,        # Mathématiques
            'pc_lv2': 2,       # PC/LV2
            'svt': 2,          # SVT
            'anglais': 2,      # Anglais écrit
            'anglais_oral': 1, # Anglais oral
            'eps': 1           # EPS
        }
        
        total_points = 0
        bonus_malus = 0
        
        # Calcul des points pour chaque matière
        for matiere, coef in coefficients.items():
            if matiere in notes:
                total_points += notes[matiere] * coef

        # Règle RM2 : Calcul bonus/malus EPS
        if 'eps' in notes:
            if notes['eps'] > 10:
                bonus_malus += notes['eps'] - 10
            else:
                bonus_malus += 10 - notes['eps']

        # Règle RM3 : Bonus épreuve facultative
        if 'epreuve_facultative' in notes and notes['epreuve_facultative'] > 10:
            bonus_malus += notes['epreuve_facultative'] - 10

        return total_points, bonus_malus

    def calculer_points_second_tour(self, notes):
        # Coefficients du second tour (RM10)
        coefficients = {
            'francais': 3,
            'mathematiques': 3,
            'pc_lv2': 2
        }
        
        total_points = 0
        for matiere, coef in coefficients.items():
            if matiere in notes:
                total_points += notes[matiere] * coef
                
        return total_points

    def determiner_statut(self, points, moyenne_cycle, nb_tentatives):
        # Premier tour
        if points >= 180:
            return "ADMIS(E)"
        elif points >= 171 and points < 180:
            if nb_tentatives <= 2:  # RM12
                return "REPÊCHABLE D'OFFICE"
            return "ÉCHEC"
        elif points >= 153:
            return "ADMIS(E) AU SECOND TOUR"
        elif points >= 144 and points < 153:
            if nb_tentatives <= 2 and moyenne_cycle >= 12:  # RM7 et RM12
                return "REPÊCHABLE SECOND TOUR"
            return "ÉCHEC"
        return "ÉCHEC"

    def generer_releve(self, candidat, notes_premier_tour, notes_second_tour=None, output_path=None):
        if output_path is None:
            output_path = f"releve_notes_{candidat['numero']}.pdf"

        doc = SimpleDocTemplate(output_path, pagesize=A4)
        elements = []

        # Style pour les titres et le contenu
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=14,
            alignment=1,
            spaceAfter=20
        )

        # En-tête du relevé
        elements.append(Paragraph("RÉPUBLIQUE DU SÉNÉGAL", title_style))
        elements.append(Paragraph("MINISTÈRE DE L'ÉDUCATION NATIONALE", title_style))
        elements.append(Paragraph("RELEVÉ DE NOTES - BFEM 2024", title_style))
        elements.append(Spacer(1, 20))

        # Informations du candidat
        infos_candidat = [
            ["Numéro de table:", candidat['numero']],
            ["Nom et Prénom:", f"{candidat['nom']} {candidat['prenom']}"],
            ["Date de naissance:", candidat['date_naissance']],
            ["Lieu de naissance:", candidat['lieu_naissance']],
            ["Établissement:", candidat['etablissement']]
        ]
        
        t_infos = Table(infos_candidat, colWidths=[100, 300])
        t_infos.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey)
        ]))
        elements.append(t_infos)
        elements.append(Spacer(1, 20))

        # Notes du premier tour
        elements.append(Paragraph("PREMIER TOUR", title_style))
        
        data_premier_tour = [
            ["Matière", "Note", "Coefficient", "Points"],
            ["Composition Française", notes_premier_tour.get('compo_franc', ''), "2", ''],
            ["Dictée", notes_premier_tour.get('dictee', ''), "1", ''],
            ["Étude de texte", notes_premier_tour.get('etude_texte', ''), "1", ''],
            ["Instruction Civique", notes_premier_tour.get('inst_civique', ''), "1", ''],
            ["Histoire-Géographie", notes_premier_tour.get('hist_geo', ''), "2", ''],
            ["Mathématiques", notes_premier_tour.get('maths', ''), "4", ''],
            ["PC/LV2", notes_premier_tour.get('pc_lv2', ''), "2", ''],
            ["SVT", notes_premier_tour.get('svt', ''), "2", ''],
            ["Anglais écrit", notes_premier_tour.get('anglais', ''), "2", ''],
            ["Anglais oral", notes_premier_tour.get('anglais_oral', ''), "1", ''],
            ["EPS", notes_premier_tour.get('eps', ''), "1", '']
        ]

        points_premier_tour, bonus_malus = self.calculer_points_premier_tour(notes_premier_tour)
        
        # Tableau des notes du premier tour
        t_premier_tour = Table(data_premier_tour, colWidths=[150, 100, 100, 100])
        t_premier_tour.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ]))
        elements.append(t_premier_tour)
        elements.append(Spacer(1, 10))

        # Total premier tour
        elements.append(Paragraph(f"Total points: {points_premier_tour}", self.styles['Normal']))
        elements.append(Paragraph(f"Bonus/Malus: {bonus_malus}", self.styles['Normal']))
        elements.append(Paragraph(f"Total général: {points_premier_tour + bonus_malus}", self.styles['Normal']))

        # Si second tour
        if notes_second_tour:
            elements.append(Spacer(1, 20))
            elements.append(Paragraph("SECOND TOUR", title_style))
            
            data_second_tour = [
                ["Matière", "Note", "Coefficient", "Points"],
                ["Français", notes_second_tour.get('francais', ''), "3", ''],
                ["Mathématiques", notes_second_tour.get('mathematiques', ''), "3", ''],
                ["PC/LV2", notes_second_tour.get('pc_lv2', ''), "2", '']
            ]
            
            points_second_tour = self.calculer_points_second_tour(notes_second_tour)
            
            t_second_tour = Table(data_second_tour, colWidths=[150, 100, 100, 100])
            t_second_tour.setStyle(TableStyle([
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ]))
            elements.append(t_second_tour)
            elements.append(Spacer(1, 10))
            elements.append(Paragraph(f"Total points second tour: {points_second_tour}", self.styles['Normal']))

        # Génération du document
        doc.build(elements)
        return output_path

# Exemple d'utilisation
def imprimer_releve(numero_table):
    generateur = ReleveNotesBFEM()
    
    # Ces données devraient venir de la base de données
    candidat = {
        "numero": numero_table,
        "nom": "DIOP",
        "prenom": "Fatou",
        "date_naissance": "15/03/2008",
        "lieu_naissance": "Dakar",
        "etablissement": "CEM Pikine"
    }
    
    notes_premier_tour = {
        'compo_franc': 15,
        'dictee': 14,
        'etude_texte': 16,
        'inst_civique': 17,
        'hist_geo': 15,
        'maths': 13,
        'pc_lv2': 14,
        'svt': 15,
        'anglais': 16,
        'anglais_oral': 15,
        'eps': 12,
        'epreuve_facultative': 13
    }
    
    # Si le candidat est au second tour
    notes_second_tour = {
        'francais': 14,
        'mathematiques': 15,
        'pc_lv2': 13
    }
    
    # Génération du relevé
    output_path = f"releves/releve_{numero_table}.pdf"
    os.makedirs("releves", exist_ok=True)
    
    generateur.generer_releve(candidat, notes_premier_tour, notes_second_tour, output_path)
    return output_path

# imprimer_releve(2)