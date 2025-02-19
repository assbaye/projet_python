from livret_scolaire import LivretScolaire



Interface_livretscolaire = LivretScolaire()

Interface_livretscolaire.add_livretscolaire(2,2.5,4.6,15.5,3.5,1)

print(Interface_livretscolaire.get_all_livretscolaires())

Interface_livretscolaire.delete_livretscolaire(2)

print(Interface_livretscolaire.get_all_livretscolaires())

