from bdd import bdd


class Matiere:

    def __init__(self):
        self.db = bdd()
        self.create_table()

    """
    Creation de la table des matieres
   
    """

    def create_table(self):

        self.db.execute(
            """
                CREATE TABLE IF NOT EXISTS matieres (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom_matiere VARCHAR(125),
                    coefficient INTEGER
                )
            
            """
        )

    """ insertion d'une matiere """

    def add_matiere(self, nom_matiere, coefficient):
        try:
            self.db.execute("INSERT INTO matieres (nom_matiere,coefficient) VALUES (?,?)",
                            ( nom_matiere, coefficient))
            return True
        except Exception:
            return False

    def get_matiere(self, matiere_id):
        return self.db.fetchone("SELECT * FROM matieres WHERE id=?", (matiere_id,))

    def getAll(self):
        return self.db.fetchall("SELECT * FROM matieres ")

    def delete_matiere(self, matiere_id):
        self.db.execute("DELETE FROM matieres WHERE id=?", (matiere_id,))