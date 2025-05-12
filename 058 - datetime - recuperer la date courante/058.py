# 058 - Calculer l'année de naissance à partir d'un âge donné
# Notions abordées : le module datetime.

# Dans cet exercice, nous allons utiliser le module datetime pour calculer l'année de naissance de quelqu'un, à partir de son âge.

# Dans cet exemple, nous allons prendre un âge de 25 ans.

# Afin de ne pas fausser les résultats, nous allons également indiquer le mois de naissance afin de vérifier si la date d'anniversaire de la personne est passée ou non.

# Nous avons donc deux variables :

# La variable age qui contient l'âge de la personne (ici : 25).

# Le mois de naissance, contenu dans la variable mois_de_naissance (ici, le mois d'octobre, soit 10).

# À partir de ces deux infos, il faut calculer l'année à laquelle est née la personne. 



# Pour valider l'exercice, vous devez récupérer l'année de naissance dans une variable nommée resultat (la variable doit être de type integer / nombre entier).


# SOLUTION
from datetime import datetime

age = 25
mois_de_naissance = 10

now = datetime.today()
annee_naissance = now.year - age

if now.month < mois_de_naissance:
    annee_naissance -= 1

resultat = annee_naissance
print(resultat)

# --------------------------

from datetime import datetime
 
age = 25
mois_de_naissance = 10
 
annee_actuelle = datetime.today().year
mois_actuel = datetime.today().month
 
resultat = annee_actuelle - age - (1 if mois_de_naissance > mois_actuel else 0)
print(resultat)


# EXPLICATION
# Pour récupérer l'année actuelle, on utilise datetime.today().year
# Pour récupérer le mois actuel, on utilise datetime.today().month
