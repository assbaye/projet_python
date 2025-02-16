from bdd import bdd  
import random

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
                numero TEXT UNIQUE,
                matiere_id INTEGER,
                candidat_id INTEGER,
                examen TEXT,
                session INTEGER,  -- Ajout de la session (1 ou 2)
                FOREIGN KEY (candidat_id) REFERENCES candidats(id),
                FOREIGN KEY (matiere_id) REFERENCES matieres(id)
            )
            """
        )

    def anonymat_existe(self, numero, session):
        """
        Vérifie si un anonymat existe déjà en base pour une session donnée.
        
        :param numero: Numéro anonymat
        :param session: Session (1 ou 2)
        :return: True si l'anonymat existe, False sinon
        """
        cursor = self.db.conn.cursor()  
        cursor.execute("SELECT 1 FROM anonymats WHERE numero = ? AND session = ?", (numero, session))
        result = cursor.fetchone()  
        return result is not None

    def generer_anonymat(self, candidat_id, matiere_id, examen, session):
        """
        Génère et insère un anonymat pour un candidat, une matière et une session donnée.
        
        :param candidat_id: Identifiant du candidat
        :param matiere_id: Identifiant de la matière
        :param examen: Nom de l'examen
        :param session: Session de l'examen (1 ou 2)
        :return: Numéro anonymat généré ou None en cas d'erreur
        """
        try:
            # Génération d'un anonymat unique avec session
            while True:
                numero_anonymat = f"{examen[:4]}-{matiere_id}-{session}-{random.randint(1000, 9999)}"
                if not self.anonymat_existe(numero_anonymat, session):
                    break

            self.db.execute(
                "INSERT INTO anonymats (numero, matiere_id, candidat_id, examen, session) VALUES (?, ?, ?, ?, ?)",
                (numero_anonymat, matiere_id, candidat_id, examen, session),
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
    
    # Génération pour la session 1
    numero_session1 = db.generer_anonymat(test_candidat_id, test_matiere_id, test_examen, 1)
    if numero_session1:
        print(f"✅ Anonymat Session 1 généré avec succès: {numero_session1}")
    else:
        print("❌ Échec de la génération de l'anonymat pour la session 1.")

    # Génération pour la session 2
    numero_session2 = db.generer_anonymat(test_candidat_id, test_matiere_id, test_examen, 2)
    if numero_session2:
        print(f"✅ Anonymat Session 2 généré avec succès: {numero_session2}")
    else:
        print("❌ Échec de la génération de l'anonymat pour la session 2.")
