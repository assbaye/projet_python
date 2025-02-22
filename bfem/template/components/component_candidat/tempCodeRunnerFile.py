import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname("__file__"), "../../../.."))
)
from bfem.database.candidat import Candidat
from bfem.database.bdd import bdd