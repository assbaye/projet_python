import sqlite3

class bdd:

    _instance = None
    @staticmethod
    def connect():
        return sqlite3.connect("examen_bfem")
    
    def __new__(cls,db_name="examen_bfem"):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.conn = sqlite3.connect(db_name)
            cls._instance.cursor = cls._instance.conn.cursor()

        return cls._instance
    
    """
     #   Execute une requete Sql
    """
    def commit(self):
        self.conn.commit()
    def execute(self,query,params=()):
        self.cursor.execute(query,params)
        self.conn.commit()
        return self.cursor
    
    """

      #  Recupere tous les les resultats d'une requete

    """

    def fetchall(self,query,params=()):

        self.cursor.execute(query,params)
        return self.cursor.fetchall()
    
    """

      #  Recupere un seul resultat 

    """

    def fetchone(self, query,params=()):
        self.cursor.execute(query,params)
        return self.cursor.fetchone()
    
    """

        # Fermer la connexion a la base de donnees

    """

    def clone(self):
        self.conn.close()
        bdd._instance = None