# projet_python

Le projet vise à développer un prototype de logiciel destiné à la gestion des données et à la délibération des candidats lors de l'examen du BFEM au Sénégal.

Participant :

- Ahmadou Khadim Kebe
- EL Hadj Samba Syll
- Ibrahima Kebe

Dictionnaires des donnes

Jury :
    - Region_IA
    - Departement_IEF
    - Localite
    - centre_examen
    - president_jury
    - telephone
    - motdepasse

Candidat:
    - Numero de table : Entier
    - Prenom_s : Chaine de caractères
    - Nom : Chaine de caractères
    - Date_naissance : Date
    - Lieu_naissance : chaine de carcateres
    - Sexe : Caractères => H/F
    - Nationalite : Chaine de caractères
    - Choix_epr_facultaive : Booleen
    - etablissement
    - Epreuve_Facultaive : Chaine de caractères
    - Aptitude_sportive : Boolean

Livret scolaire:
    - Nombre_de_fois : Entier => Nombre de tentative a l'examen
    - Moyen_6e : décimal => Moyenne générale en classe de 6e
    - Moyen_5e : décimal => Moyenne générale en classe de 5e
    - Moyen_4e : décimal => Moyenne générale en classe de 4e
    - Moyen_3e : décimal => Moyenne générale en classe de 3e
    - Moyen_cycle : décimal  => Moyenne du cumul des 4 années
    - candidat_id

Evaluation:  
    - note
    - Matiere_id
    - candidat_id
Matiere:
    - nom
    - Coeff

Fonctionnalités à rendre:

- Paramétrage jury :
  - prérequis : il faut avoir un compte admin
  - description :  Insertion d'un jury

- Crud Candidats :
  - prérequis : Il faut se connecter et être un membre du jury
  - description : on peut insérer, modifier , supprimer et récupérer un candidat
    - Insérer : on doit voir les données du candidats
    - modifier : on peut modifier les donnes d'un candidats selon son identifiant
    - supprimer : Suppression d'un candidat.
    - sélectionner : Récupération d'un candidat spécifique ou de tous les candidats.

- generateur automatique d'anonymat pour la correction et la saisie au 1er et 2nd tour des notes
  - prérequis : il faut avoir des candidats
  - description : Pour chaque examen, le candidat aura un numéro d'identifiant unique pour chaque matières
     Table : < Numéro_candidat_matiere>
        - numero
        - matiere_id
        - candidat_id
        - Examen

- Suivi de la délibération pour la 1er et 2nd tour des épreuves
  - prerequis : Il faut enregistrer tous les notes
  - description : Les deliveration se fait en meme temps qu'on enregistre les notes
    - Il faut entrer les notes pour chaque matière et calculer les résultats.
    - Calcule des résultats et attribution des statuts (admis, repêchage, recalé).

- Gestion des repêchages
  - prerequis : Livret scolaire et note du candidat
  - description : Détermine les candidats pouvant bénéficier d’un repêchage en fonction de leurs notes et de leurs résultats scolaires.

- Impression en pdf de toutes les listes (candidats, anononymats,resultats, pv delibeartion)
  
  - prerequis :
    - il faut avoir des donnees pour chaque categorie 
  - description :
    Impression des listes de :
      - Candidats
      - Anonymats (numero de matiere,)
      - Résultats
      - Procès-verbaux de délibération
    

- Statistiques
  - Génération de statistiques détaillées sur les résultats (taux de réussite, répartition des moyennes,     comparaison entre centres, etc.).

- Générateur de relevés de notes pour le 1er et le 2nd tour des épreuves
  - prerequis : notes du 1er et 2nd tour
  - description : creation automatique d'un relevé de notes pour chaque candidat et pour chaque tour examen 

- Intégrez les donnees sur le prototype pour faire les tests
  - Vérification du bon fonctionnement du système avec des données de test
