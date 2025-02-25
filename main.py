import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bfem.template.MyApp import MyApp
from bfem.database.candidat import Candidat
from bfem.database.matiere import Matiere
from bfem.database.anonymous import AnonymatDatabase
from bfem.database.examen import Examen

if __name__ == '__main__':
    # an= AnonymatDatabase().getAll()

    # print(an)
    # an= AnonymatDatabase().verifie_anonymat(1,5435,"Session 1")
    # # print(an)
    # print(Candidat().get_all_candidate())
    # print(Matiere().getAll())
    # print(AnonymatDatabase().getAll())
    
    MyApp().run()

    # interf = Examen().deliverer("Session 1")

    # Examen().add_note(10,4882)

    # print(Examen().get_all_note())

