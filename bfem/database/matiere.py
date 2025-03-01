from .bdd import bdd


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
                    coefficient INTEGER,
                    UNIQUE(nom,coefficient)
                )
            
            """
        )
        self.add_column_if_not_exists("bonus","INTEGER",0)

    def add_matiere(self, nom_matiere, coefficient,bonus):
        try:
            self.db.execute("INSERT INTO matieres (nom_matiere,coefficient) VALUES (?,?,?)",( nom_matiere, coefficient,bonus))
            return True
        except Exception as e:
            print(f"Erreur lors de l'ajout du candidat : {str(e)}")  # Affichage de l'erreur
            return False

    def get_matiere(self, matiere_id):
        return self.db.fetchone("SELECT * FROM matieres WHERE id=?", (matiere_id,))

    def getAll(self):
        return self.db.fetchall("SELECT * FROM matieres")
    
    def getIds(self):
        return self.db.fetchall("SELECT id FROM matieres ")
        
    def delete_matiere(self, matiere_id):
        self.db.execute("DELETE FROM matieres WHERE id=?", (matiere_id,))
        
    def update_matiere(self, matiere_id, nouveau_nom, nouveau_coefficient):
        query = "UPDATE matieres SET nom_matiere = ?, coefficient = ? WHERE id = ?"
        self.db.execute(query, (nouveau_nom, nouveau_coefficient, matiere_id))

    def add_column_if_not_exists(self, column_name, column_type, default_value):
   
        columns = [col[1] for col in self.db.fetchall("PRAGMA table_info(matieres)")]

        if column_name not in columns:
            try:
                self.db.execute(
                    f"ALTER TABLE matieres ADD COLUMN {column_name} {column_type} DEFAULT {default_value}"
                )
                print(f"Colonne '{column_name}' ajoutée avec succès.")
            except Exception as e:
                print(f"Erreur lors de l'ajout de la colonne : {e}")
        else:
            print(f"La colonne '{column_name}' existe déjà.")

            