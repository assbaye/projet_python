from matiere import Matiere


matiere_interface = Matiere()

matiere_interface.add_matiere("Mathematique", 4)
matiere_interface.add_matiere("PC", 2)
print(matiere_interface.get_matiere(2))
matiere_interface.delete_matiere(2)
matiere_interface.update_matiere(1,"Mathématique",3)
print(matiere_interface.getAll())
