from bdd import bdd

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

""""
Candidat 
    => create_table()
    => add_candidate(params...)
    => get_candidate(candidate_id)
    => get_all_candidate(candidate_id)
    => delete_candidat(candidat_id)
    => update(candidate_id, params)
"""

""" Gestion des candidats """
class Candidat:

    
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
                        sexe CHAR(2) CHECK(sexe IN ('H','F')),
                        nationalite Text NOT NULL,
                        choix_epr_facultative BOOL NOT NULL DEFAULT(0),
                        epr_facultative VARCHAR(125) CHECK (epr_facultative IN ('Couture','Dessin','Musique','Neutre')),
                        etablissement VARCHAR(250),
                        aptitude_sportive BOOL default(1)
                        )"""
                        )
        
    def add_candidate(self,prenom,nom,date_naissance,lieu_naissance,sexe,nationalite,choix_epr_facultative,epr_facultative,etablissement,aptitude_sportive):
        
            self.db.execute("INSERT INTO candidats (prenom,nom,date_naissance,lieu_naissance,sexe,nationalite,choix_epr_facultative,epr_facultative,etablissement,aptitude_sportive) VALUES (?,?,?,?,?,?,?,?,?,?)",(prenom,nom,date_naissance,lieu_naissance,sexe,nationalite,choix_epr_facultative,epr_facultative,etablissement,aptitude_sportive))
            
       
    
    def get_candidate(self,candidate_id):

        try :
            return self.db.fetchone("SELECT * FROM candidats WHERE id=?",(candidate_id,))
        except Exception:
            return False
        

    def get_all_candidate(self):

        return self.db.fetchall("SELECT * FROM candidats")
    


    def delete_candidate(self,candidate_id):
        try:
         self.db.execute("DELETE FROM candidats WHERE id=?",(candidate_id,))
         return True
        except Exception :
            return False
    

    def update_candidate(self,candidate_id,prenom = None,nom= None,date_naissance= None,lieu_naissance= None,sexe= None,nationalite= None,choix_epr_facultative= None,epr_facultative= None,etablissement= None,aptitude_sportive= None):
       
       query = "UPDATE candidats SET "
       values = []
       
       if prenom:
            query += "prenom = ?, "
            values.append(prenom)
        
       if nom:
            query += "nom =?, "
            values.append(nom)

       if date_naissance:
            query += "date_naissance = ?, "
            values.append(date_naissance)

       if lieu_naissance:
        query += "lieu de naissance = ?, "
        values.append(lieu_naissance)

       if sexe :
            query += "sexe= ?, "
            values.append(sexe)

       if nationalite:
            query +="nationalite=?, "
            values.append(nationalite)

       if choix_epr_facultative:
        query+="choix_epr_facultative=?, "
        values.append(choix_epr_facultative)

       if epr_facultative:
            query+= "epr_facultative= ?, "
            values.append(epr_facultative)

       if etablissement:
            query += "etablissement= ?, "
            values.append(etablissement)

       if aptitude_sportive:
            query += "aptitude_sportive= ?, "
            values.append(aptitude_sportive)

       query = query.rstrip(", ")
       query += " WHERE id= ?"
       values.append(candidate_id)

        
       self.db.execute(query,(values))

      
          



