from bfem.database.bdd import bdd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os
#     - Numero de table : Entier
#     - Prenom_s : Chaine de caractères
#     - Nom : Chaine de caractères
#     - Date_naissance : Date
#     - Lieu_naissance : chaine de carcateres
#     - Sexe : Caractères => H/F
#     - Nationalite : Chaine de caractères
#     - Choix_epr_facultaive : Booleen
#     - etablissement
#     - Epreuve_Facultative : Chaine de caractères
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
                        epr_facultative VARCHAR(125) CHECK (epr_facultative IN ('Couture','Dessin','Musique','Neutre')),
                        etablissement VARCHAR(250),
                        aptitude_sportive BOOL default(1),
                        lv2_pc VARCHAR(10) ,
                        type_candidats VARCHAR(125) CHECK (type_candidats IN ('Officiel','Libre'))
                        )"""
                        )
        # Ajouter les nouvelles colonnes si elles n'existent pas déjà
        existing_columns = [col[1] for col in self.db.fetchall("PRAGMA table_info(candidats)")]
        new_columns = {
           "moyenne_6e": "FLOAT",
           "moyenne_5e": "FLOAT",
           "moyenne_4e": "FLOAT",
           "moyenne_3e": "FLOAT",
           "lv2": "VARCHAR(125)",
           "type_candidat": "VARCHAR(125)",
           "nombre_fois": "INTEGER"
       }

        for col, col_type in new_columns.items():
            if col not in existing_columns:
                self.db.execute(f"ALTER TABLE candidats ADD COLUMN {col} {col_type}")
        

    def add_candidate(self, prenom, nom, date_naissance, lieu_naissance, sexe, nationalite, epr_facultative, etablissement, aptitude_sportive,lv2,type):
            try:
                self.db.execute("INSERT INTO candidats (prenom, nom, date_naissance, lieu_naissance, sexe, nationalite, epr_facultative, etablissement, aptitude_sportive,lv2_pc,type_candidats) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                    (prenom, nom, date_naissance, lieu_naissance, sexe, nationalite,  epr_facultative, etablissement, aptitude_sportive,lv2,type))
               
                return self.db.fetchall("SELECT  * FROM candidats ORDER BY id DESC  LIMIT 1")
            except Exception as e:
                print(f"Erreur lors de l'ajout du candidat : {str(e)}")  # Affichage de l'erreur
                return False
        

  
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
    

    def update_candidate(self,candidate_id,prenom = None,nom= None,date_naissance= None,lieu_naissance= None,sexe= None,nationalite= None,epr_facultative= None,etablissement= None,aptitude_sportive= None,type_candidats=None):
       
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

      

       if epr_facultative:
            query+= "epr_facultative= ?, "
            values.append(epr_facultative)
       
       if type_candidats:
            query+= "type_candidats= ?, "
            values.append(type_candidats)

       if etablissement:
            query += "etablissement= ?, "
            values.append(etablissement)

       if aptitude_sportive:
            query += "aptitude_sportive= ?, "
            values.append(aptitude_sportive)
     #   if moyenne_6e:
     #        query += "moyenne_6e= ?, "
     #        values.append(moyenne_6e)
     #   if moyenne_5e:
     #        query += "moyenne_5e= ?, "
     #        values.append(moyenne_5e)
     #   if moyenne_4e:
     #        query += "moyenne_4e= ?, "
     #        values.append(moyenne_4e) 
     #   if moyenne_3e:
     #        query += "moyenne_3e= ?, "
     #        values.append(moyenne_3e)
     #   if lv2:
     #        query += "lv2= ?, "
     #        values.append(lv2)   
     #   if type_candidat:
     #        query += "type_candidat= ?, "
     #        values.append(type_candidat) 
     #   if nombre_fois:
     #        query += "nombre_fois= ?, "
     #        values.append(nombre_fois)
             
       query = query.rstrip(", ")
       query += " WHERE id= ?"
       values.append(candidate_id)

        
       self.db.execute(query,(values))

      
          



