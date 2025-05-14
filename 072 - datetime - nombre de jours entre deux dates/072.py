# 072 - Calculer le nombre de jours entre deux dates
# Notions abordées : le module datetime.

# Dans cet exercice, nous allons calculer le nombre de jours entre deux dates.

# La date de départ que nous allons utiliser est le 2 juillet 2014 et la date de fin le 11 juillet 2018.

# Le nombre de jours entre ces deux dates est 1470.

# À vous de trouver le code qui permet de calculer automatiquement le nombre de jours entre ces deux dates, grâce au module datetime.


# SOLUTION
from datetime import date

date_1 = date(year=2014, month=7, day=2)
date_2 = date(year=2018, month=7, day=11)

diff = date_2 - date_1
print(diff.days)


# EXPLICATION
# Pour faire des calculs avec des dates, on utilise le module datetime et la classe date.
