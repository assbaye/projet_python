import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bfem.database.candidat import Candidat



# on instancie l'interface de classe

Interface_candidat =  Candidat()



# on ajoute un candidat 

print(Interface_candidat.add_candidate("ABLAYE","Ndiaye","21/12/2003","louga","M","Senegalaise","0","Neutre","CEM dielerlou","False","12","13","14","15","PC","officiel","0"))

print(Interface_candidat.add_candidate("FATOU","Gaye","21/12/2002","Dakar","F","Senegalaise","0","Neutre","CEM Commune","False","11","10","12","14","LV2","libre","2"))


# on recupre les candidat 

print(Interface_candidat.get_all_candidate())

print(Interface_candidat.get_candidate(1))

# on modifie le candidat numero 2

# Interface_candidat.update_candidate(1,prenom="cana")


print(Interface_candidat.get_candidate(2))
