from database.bdd import bdd


class Jury :

    def __init__(self):
        self.bd = bdd()
        self.create_table()
    
    """
    Creation de la table des taches 
     - Region_IA
    - Departement_IEF
    - Localite
    - centre_examen
    - president_jury
    - telephone
    - motdepasse

    """
    def create_table(self):
        self.db.execute(
            """
                CREATE TABLE IF NOT EXISTS jurys (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    region_ia VARCHAR(125),
                    departement_ief VARCHAR(125),
                    localite TEXT,
                    centre_examen VARCHAR(125),
                    president_jury VARCHAR(255) UNIQUE,
                    telephone VARCHAR(255),
                    motdepasse TEXT
                )
            
            """
        )
