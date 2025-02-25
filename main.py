import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../..")))

from bfem.template.MyApp import MyApp
from bfem.database.candidat import Candidat
from bfem.database.matiere import Matiere
from bfem.database.anonymous import AnonymatDatabase


if __name__ == '__main__':
    # print(Candidat().get_all_candidate())
    # print(Matiere().getAll())
    # print(AnonymatDatabase().getAll())

    MyApp().run()
   

