from matiere import Matiere
"""
    Compo_Franc 2
    Dictee  1
    Etude de texte 1
    Intructuction Civique 1
    Histoire geographie 2
    Mathematique    4
    Pc/lv2  2
    SVT     2
    Anglais 2
    Anglais_oral    1
    Eps     
    epreuve Facultative 
"""


matiere_interface = Matiere() 
# for mat in matiere_interface.getAll():
#     matiere_interface.delete_matiere(mat[0])
matiere_interface.add_matiere("Mathematique", 4)
matiere_interface.add_matiere("Compo_Franc", 2)
matiere_interface.add_matiere("Dictee", 1)
matiere_interface.add_matiere("Etude de texte", 1)
matiere_interface.add_matiere("Pc/LV2", 2)
matiere_interface.add_matiere("Svt", 2)
matiere_interface.add_matiere("Anglais", 2)
matiere_interface.add_matiere("Anglais_oral", 2)
# matiere_interface.add_matiere("PC", 2)
print(matiere_interface.get_matiere(2))
# matiere_interface.delete_matiere(2)
# matiere_interface.update_matiere(1,"Mathématique",3)
print(matiere_interface.getAll())

