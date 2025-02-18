from bfem.database.bdd import bdd

#  - Numero de table : Entier
#     - Prenom_s : Chaine de caractères
#     - Nom : Chaine de caractères
#     - Date_naissance : Date
#     - Lieu_naissance : chaine de carcateres
#     - Sexe : Caractères => H/F
#     - Nationalite : Chaine de caractères
#     - Choix_epr_facultaive : Booleen
#     - etablissement
#     - Epreuve_Facultaive : Chaine de caractères
#     - Aptitude_sportive : Boolean


class Candidat:

    """ Gestion des candidats """
    def __init__(self):
        self.db = bdd()
        self.create_table()
    

    # Creation de la base de donnees des candidats si tel n'est pas le cas
    
    def create_table(self):
        self.db.execute(""" CREATE TABLE IF NOT EXISTS candidats (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        prenom VARCHAR(125) NOT NULL,
                        nom VARCHAR(125) NOT NULL,
                        date_naissance DATE NOT NULL,
                        lieu_naissance VARCHAR(125) NOT NULL,
                        sexe CHAR(2) CHECK(sexe IN ('M','F')),
                        nationalite Text NOT NULL,
                        choix_epr_facultative BOOL NOT NULL DEFAULT(0),
                        epr_facultative VARCHAR(125) CHECK (epr_facultative IN ('Couture','Dessin','Musique','Neutre')),
                        etablissement VARCHAR(250),
                        aptitude_sportive BOOL default(1)
                        )"""
                        )
        
    def add_candidate(self, prenom, nom, date_naissance, lieu_naissance, sexe, nationalite, choix_epr_facultative, epr_facultative, etablissement, aptitude_sportive):
            try:
                self.db.execute("INSERT INTO candidats (prenom, nom, date_naissance, lieu_naissance, sexe, nationalite, choix_epr_facultative, epr_facultative, etablissement, aptitude_sportive) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (prenom, nom, date_naissance, lieu_naissance, sexe, nationalite, choix_epr_facultative, epr_facultative, etablissement, aptitude_sportive))
                self.db.commit()  
                return True
            except Exception as e:
                print(f"Erreur lors de l'ajout du candidat : {str(e)}")  # Affichage de l'erreur
                return False
        
    
    def get_candidate(self,candidate_id):

        try :

            return self.db.fetchall("SELECT * FROM candidats WHERE id=?",(candidate_id,))
        except Exception:
            return False

    def delete_candidate(self,candidate_id):
        try:
         self.db.execute("DELETE FROM candidats WHERE id=?",(candidate_id,))
         return True
        except Exception :
            return False
        
    def getAll(self):
        return self.db.fetchall("SELECT * FROM candidats")



