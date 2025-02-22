from .bdd import bdd  


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
                FOREIGN KEY (matiere_id) REFERENCES matieres(id)
            )
            """
        )

    def get_anomonymat_by_matiere(self,matiere_id):
        return self.db.fetchall("SELECT * FROM anonymats WHERE matiere_id=?",(matiere_id, ))

    def getAll(self):
        return self.db.fetchall("SELECT * FROM anonymats ")

    def generer_anonymat(self, candidat_id, matiere_id, examen):
        """
        Génère et insère un anonymat pour un candidat et une matière donnée.
        
        :param candidat_id: Identifiant du candidat
        :param matiere_id: Identifiant de la matière
        :param examen: Nom de l'examen
        :return: Numéro anonymat généré ou None en cas d'erreur
        """
        try:
            numero_anonymat = candidat_id * 100 + matiere_id  # Génération d'un numéro anonymat unique
            self.db.execute(
                "INSERT INTO anonymats (numero, matiere_id, candidat_id, examen) VALUES (?, ?, ?, ?)",
                (numero_anonymat, matiere_id, candidat_id, examen),
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
    
    numero = db.generer_anonymat(test_candidat_id, test_matiere_id, test_examen)
    if numero:
        print(f"Anonymat généré avec succès: {numero}")
    else:
        print("Échec de la génération de l'anonymat.")
