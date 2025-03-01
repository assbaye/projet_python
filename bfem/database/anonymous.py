from .bdd import bdd  

from random import randint

class AnonymatDatabase:
    def __init__(self):
        """
        Initialise la connexion à la base de données et crée la table des anonymats si elle n'existe pas.
        """
        self.db = bdd()
        self.create_tables()

    def create_tables(self):
        """
        Crée la table `anonymats` si elle n'existe pas déjà.
        """
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS anonymats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER UNIQUE,
                matiere_id INTEGER,
                candidat_id INTEGER,
                examen TEXT,
                FOREIGN KEY (candidat_id) REFERENCES candidats(id),
                FOREIGN KEY (matiere_id) REFERENCES matieres(id),
                UNIQUE(matiere_id,candidat_id,examen)
            )
            """
        )
      
    
    def verifie_anonymat(self,matiere_id,anonymat,session):
        # print(session)
        return self.db.fetchall("""
                                SELECT e.note
                                FROM anonymats a 
                                JOIN examens e ON e.anonymat_id =a.numero 
                                WHERE a.matiere_id=? and a.examen=? and a.numero=?""",(matiere_id,session,anonymat ))

    def get_anomonymat_by_matiere(self,matiere_id,session):
        return self.db.fetchall("SELECT * FROM anonymats WHERE matiere_id=? and examen=?",(matiere_id,session ))

    def getAll(self):
        return self.db.fetchall("SELECT * FROM anonymats ") 

    def get_matieres(self):
        query = "SELECT nom_matiere FROM matieres"
        result = self.db.fetchall(query)
        return [row[0] for row in result]
    
    def afficher_anonymats(self, matiere):
        query = """
            SELECT candidats.id, anonymats.numero
            FROM anonymats
            JOIN candidats ON anonymats.candidat_id = candidats.id
            JOIN matieres ON anonymats.matiere_id = matieres.id
            WHERE matieres.nom_matiere = ?
        """
        return self.db.fetchall(query, (matiere,))
    
    def generer_anonymat(self, candidat_id, matiere_id, examen):
        """
        Génère et insère un anonymat pour un candidat et une matière donnée, en tenant compte de la session.

        :param candidat_id: Identifiant du candidat
        :param matiere_id: Identifiant de la matière
        :param session: Numéro de la session (1 ou 2)
        :param examen: Nom de l'examen
        :return: Numéro anonymat généré ou None en cas d'erreur
        """
        try:
            numero_anonymat = int(candidat_id) * randint(100,10000) + int(matiere_id)  # Génération d'un numéro anonymat unique
            self.db.execute(
                "INSERT INTO anonymats (numero, matiere_id, candidat_id, session, examen) VALUES (?, ?, ?, ?, ?)",
                (numero_anonymat, matiere_id, candidat_id,examen),
            )
            return numero_anonymat
        except Exception as e:
            print(f"Erreur lors de la génération de l'anonymat: {e}")
            return None

# Partie test
if __name__ == "__main__":
    db = AnonymatDatabase()

    test_candidat_id = 1
    test_matiere_id = 2
    test_examen = "BFEM 2025"

    # Génération anonymat pour la session 1
    numero_session_1 = db.generer_anonymat(test_candidat_id, test_matiere_id, 1, test_examen)
    if numero_session_1:
        print(f"Anonymat session 1 généré avec succès: {numero_session_1}")
    else:
        print("Échec de la génération de l'anonymat pour la session 1.")

    # Génération anonymat pour la session 2
    numero_session_2 = db.generer_anonymat(test_candidat_id, test_matiere_id, 2, test_examen)
    if numero_session_2:
        print(f"Anonymat session 2 généré avec succès: {numero_session_2}")
    else:
        print("Échec de la génération de l'anonymat pour la session 2.")
