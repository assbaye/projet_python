from bdd import bdd


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

        self.db.execute("INSERT INTO examens (note,anonymat_id) VALUES(?,?)",(note,anonymat_id))
    
    def get_all_note(self):

        return self.db.fetchall("SELECT * FROM examens ")
    
    def get_note(self,anonymat_id):

        return self.db.fetchone("SELECT * FROM examens WHERE anonymat_id=?",(anonymat_id,))
    
    def update_note(self,anonymat_id,note):

        self.db.execute("UPDATE examens SET note=? WHERE anonymat_id=?",(note,anonymat_id,))
    
    def delete_note(self,anonymat_id):

        self.db.execute("DELETE FROM examens WHERE anonymat_id=?",(anonymat_id,))
        
        




