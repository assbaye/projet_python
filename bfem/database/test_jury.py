from jury import Jury




jury_interface = Jury()


# ajouter un jury 

jury_interface.add_jury("Thies","Thilmakha","pekesse","Cem 2","Ousamne Sylla","770987655","Ndiaye7655")
print(jury_interface.getAll())
jury_interface.add_jury("Louga","kebemer","zone2","Cem 2","Ibrahima Kaby","770000000","Kaby0000")

jury_interface.delete_jury(1)



# login : telephone et Mot de passe 
print(jury_interface.login("770000000","Kaby0000"))
# print(jury_interface.getAll())