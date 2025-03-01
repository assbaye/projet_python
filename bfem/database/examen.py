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

    def get_notes_by_canidate(self,candidat_id,session):
        query = """
        SELECT m.nom_matiere, e.note, m.bonus,m.coefficient
        FROM examens e
        JOIN anonymats a ON e.anonymat_id = a.numero
        JOIN matieres m ON a.matiere_id = m.id
        WHERE a.candidat_id = ? AND a.examen = ?
        """
        return self.db.fetchall(query,(candidat_id,session))

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

    def getAllnotebyCanidat(self,candidat_id,session):
        query = """
            SELECT 
                e.note,
                m.nom_matiere,
                m.bonus,
                a.examen AS session
            FROM 
                examens e
            JOIN 
                anonymats a ON e.anonymat_id = a.numero
            JOIN 
                matieres m ON a.matiere_id = m.id
            WHERE 
                a.candidat_id = ? AND a.examen = ?
            ORDER BY 
                m.nom_matiere;

        """
        return self.db.fetchall(query,(candidat_id,session))
    
    def sum (self,candidat_id,session):
        query = """
        SELECT 
            SUM(e.note * m.coefficient) AS total_pondere,
            SUM(m.coefficient) AS total_coefficients
        FROM  
            examens e
        JOIN 
            anonymats a ON e.anonymat_id = a.numero
        JOIN 
            matieres m ON a.matiere_id = m.id
        WHERE 
            a.candidat_id = ? AND a.examen = ?;
        """
        return self.db.fetchall(query,(candidat_id,session))