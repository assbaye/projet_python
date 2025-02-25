from .bdd import bdd


class Examen():


    def __init__(self):
        self.db = bdd()
        self.create_table()

    def create_table(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS examens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        note INTEGER,
                        anonymat_id BIGINTEGER UNIQUE,
                        FOREIGN KEY (anonymat_id) REFERENCES anonymats(id)
                         )"""
                        )
    
    def add_note(self, note, anonymat_id):
        try :
            self.db.execute("INSERT INTO examens (note,anonymat_id) VALUES(?,?)",(note,anonymat_id))
            return True
        except Exception as e:
            print(e)
            return False
    
    def get_all_note(self):

        return self.db.fetchall("SELECT * FROM examens ")
    # def get_all_note_by_session(self,session):
        # return self.db.fetchall("SELECT * FROM examens WHERE ")
    
    def get_note(self,anonymat_id):

        return self.db.fetchone("SELECT * FROM examens WHERE anonymat_id=?",(anonymat_id,))
    
    def update_note(self,anonymat_id,note):

        self.db.execute("UPDATE examens SET note=? WHERE anonymat_id=?",(note,anonymat_id,))

    def getnote_matiereby_session(self,id_matiere,session):

        query = """
            SELECT 
                e.note,
                a.numero AS anonymat,
               
                a.candidat_id
                
            FROM 
                examens e
            JOIN 
                anonymats a ON e.anonymat_id = a.id
            JOIN 
                matieres m ON a.matiere_id = m.id
            WHERE 
                a.matiere_id = ? 
                AND a.examen = ?
            """
        return self.db.fetchall(query,(id_matiere,session))
      


    def delete_note(self,anonymat_id):

        self.db.execute("DELETE FROM examens WHERE anonymat_id=?",(anonymat_id,))
        
    def deliverer (self,session):
        try:
         return self.db.fetchall(" SELECT c.id, c.nom, c.prenom, a.numero, m.nom_matiere,m.coefficient, ls.nombre_tentative,ls.moyen6a,ls.moyen5e,ls.moyen4e,ls.moyen3e FROM candidats c LEFT JOIN anonymats a ON c.id = a.id_candidat LEFT JOIN livret_scolaires ls ON c.id = ls.candidat_id LEFT JOIN matieres m ON a.matiere_id = m.id LEFT JOIN examens e ON c.id = candidat_id WHERE a.examen =? ",(session,))
        except Exception as e:
           print(e)