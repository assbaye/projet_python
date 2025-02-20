
from .bdd import bdd 



class LivretScolaire():


    def __init__(self):
        self.db = bdd()
        self.create_table()

    def create_table(self):

        self.db.execute(""" CREATE TABLE IF NOT EXISTS livret_scolaires (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_tentative INTEGER NOT NULL,
                        moyen6e FLOAT NOT NULL,
                        moyen5e FLOAT NOT NULL,
                        moyen4e FLOAT NOT NULL,
                        moyen3e FLOAT NOT NULL,
                        candidat_id INTEGER NOT NULL UNIQUE,
                        FOREIGN KEY (candidat_id) REFERENCES candidats(id)
                        )
                        """
                    )

    def add_livretscolaire(self,nombre_tentative,moyen6e,moyen5e,moyen4e,moyen3e,candidat_id):

        self.db.execute("INSERT INTO livret_scolaires (nombre_tentative,moyen6e,moyen5e,moyen4e,moyen3e,candidat_id) VALUES(?,?,?,?,?,?)",(nombre_tentative,moyen6e,moyen5e,moyen4e,moyen3e,candidat_id))
    
    def get_livretscolaire(self,candidat_id):
       try:
        return self.db.fetchone("SELECT * FROM livret_scolaires  WHERE candidat_id=?",(candidat_id,))
       except Exception:
          return False
       
    def get_all_livretscolaires(self):
       
       return self.db.fetchall("SELECT * FROM livret_scolaires")
    
    def delete_livretscolaire(self,candidat_id):
       
       try:
          self.db.execute("DELETE FROM livret_scolaires WHERE candidat_id=?",(candidat_id,))
          return True
       except Exception:
          return False
       
    def update_livretscolaire(self,candidat_id,nombre_tentative=None,moyen6e=None,moyen5e=None,moyen4e=None,moyen3e=None):
       
        query = "UPDATE livret_scolaires SET"
        values = []

        if nombre_tentative:
          query +="nombre_tentative =?, "
          values.append(nombre_tentative)

        if moyen6e:
          query +="moyen6e=?, "
          values.append(moyen6e)
        
        if moyen5e:
          query +="moyen5e= ?, "
          values.append(moyen5e)
        if moyen4e:
           query +="moyen4e= ?, "
           values.append(moyen4e)
        if moyen3e :
           query +="moyen3e= ?, "
        
        query = query.rstrip(", ")
        query += "WHERE candidat_id= ?"

        values.append(candidat_id)

        self.db.execute(query,(values))
       

