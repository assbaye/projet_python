from bfem.database.bdd import bdd
from hashlib import sha256


"""
  - Region_IA
    - Departement_IEF
    - Localite
    - centre_examen
    - president_jury
    - telephone
    - motdepasse
"""

class Jury :

    def __init__(self):
        self.db = bdd()
        self.create_table()
    
    """
    Creation de la table des jury
   
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
    
    """ insertion d'un jury """

    def add_jury(self,region_ia,departement_ief,localite,centre_examen,president_jury,telephone,motdepasse):
        try:
            password_has = sha256(motdepasse.encode()).hexdigest()
            self.db.execute("INSERT INTO jurys (region_ia,departement_ief,localite,centre_examen,president_jury,telephone,motdepasse) VALUES (?,?,?,?,?,?,?)",(region_ia,departement_ief,localite,centre_examen,president_jury,telephone,password_has))
            return True
        except Exception:
            return False
    
    def login(self, Telephone, motdepasse):
    # Hachage du mot de passe
        password_hash = sha256(motdepasse.encode()).hexdigest()
        Jury = self.db.fetchone("SELECT id FROM jurys WHERE telephone=? AND motdepasse=?", (Telephone, password_hash))

        return Jury[0] if Jury is not None else None
    def get_jury(self,jury_id):
        return self.db.fetchone("SELECT * FROM jurys WHERE id=?", (jury_id,))

    def getAll(self):
        return self.db.fetchall("SELECT * FROM jurys ")

    def  delete_jury(self,jury_id):
        self.db.execute("DELETE FROM jurys WHERE id=?",(jury_id,))
    
    


