import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bfem.template.MyApp import MyApp
from bfem.database.candidat import Candidat
from bfem.database.matiere import Matiere
from bfem.database.anonymous import AnonymatDatabase
from bfem.database.examen import Examen
from bfem.database.livret_scolaire import LivretScolaire
if __name__ == '__main__':
   
    
    MyApp().run()

   
    # print(Examen().getAllnotebyCanidat(1,"Session 1"))
    # print(LivretScolaire().get_livretscolaire(1))
    # print(list(Candidat().get_all_candidate()))
    # print(Examen().get_notes_by_canidate(1,"Session 1"))