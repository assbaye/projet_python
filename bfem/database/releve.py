from bdd import bdd  # type: ignore
from reportlab.lib.pagesizes import A4  # type: ignore
from reportlab.pdfgen import canvas  # type: ignore
import os  # type: ignore


class ReleveNotes:
    def __init__(self):
        self.db = bdd()

    def get_notes_candidat(self, candidat_id):
        """
        Récupère les notes du candidat via les anonymats.
        """
        query = """
       SELECT m.nom_matiere, e.note, m.coefficient
       FROM examens e
       JOIN anonymats a ON e.anonymat_id = a.id
       JOIN matieres m ON a.matiere_id = m.id
       JOIN candidats c ON a.candidat_id = c.id
       WHERE c.id = ?;


        """
        return self.db.fetchall(query, (candidat_id,))

    def get_candidat_info(self, candidat_id):
        """
        Récupère les informations du candidat.
        """
        query = """
        SELECT id, prenom, nom, etablissement
        FROM candidats
        WHERE id = ?
        """
        return self.db.fetchone(query, (candidat_id,))

    def calcul_moyenne(self, notes):
        """
        Calcule la moyenne pondérée d'un candidat.
        """
        if not notes:
            return 0
        total_points = sum(note * coeff for _, note, coeff in notes)
        total_coeff = sum(coeff for _, _, coeff in notes)
        return round(total_points / total_coeff, 2) if total_coeff > 0 else 0

    def determine_statut(self, moyenne):
        """
        Détermine le statut du candidat en fonction de sa moyenne.
        """
        if moyenne >= 10:
            return "Admis"
        elif moyenne >= 8:
            return "Repêchage"
        else:
            return "Recalé"

    def generer_releve(self, candidat_id):
        """
        Génère un relevé de notes en PDF pour un candidat.
        """
        candidat = self.get_candidat_info(candidat_id)
        notes = self.get_notes_candidat(candidat_id)

        if not candidat:
            print("Aucune information trouvée pour ce candidat.")
            return
        if not notes:
            print("Aucune note trouvée pour ce candidat.")
            return

        candidat_id, prenom, nom, etablissement = candidat
        moyenne = self.calcul_moyenne(notes)
        statut = self.determine_statut(moyenne)

        dossier = "assets/releves"
        os.makedirs(dossier, exist_ok=True)
        filename = f"{dossier}/Releve_{candidat_id}.pdf"

        try:
            c = canvas.Canvas(filename, pagesize=A4)
            c.setFont("Helvetica", 12)

            # En-tête
            c.drawString(200, 800, "République du Sénégal")
            c.drawString(200, 785, "Ministère de l'Éducation Nationale")
            c.drawString(220, 770, "Relevé de Notes")

            # Infos candidat
            c.drawString(100, 740, f"Numéro de Candidat : {candidat_id}")
            c.drawString(100, 725, f"Nom : {nom}")
            c.drawString(100, 710, f"Prénom(s) : {prenom}")
            c.drawString(100, 695, f"Établissement : {etablissement}")

            # Tableau des notes
            y = 670
            c.drawString(100, y, "Matière")
            c.drawString(300, y, "Note")
            c.drawString(400, y, "Coefficient")
            y -= 20
            c.line(100, y + 10, 500, y + 10)

            for matiere, note, coeff in notes:
                c.drawString(100, y, matiere)
                c.drawString(300, y, str(note))
                c.drawString(400, y, str(coeff))
                y -= 20

            # Moyenne et statut
            y -= 20
            c.drawString(100, y, f"Moyenne Générale : {moyenne}")
            c.drawString(300, y, f"Statut : {statut}")

            c.save()
            print(f"Relevé de notes généré : {filename}")
        except Exception as e:
            print(f"Erreur lors de la génération du relevé : {e}")


# --- Test ---
if __name__ == "__main__":
    releve = ReleveNotes()
    candidat_id = 1  # ID du candidat à tester
    releve.generer_releve(candidat_id)

