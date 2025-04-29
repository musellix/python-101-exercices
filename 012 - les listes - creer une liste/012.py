# 012 - Créer une liste de nombres de 5 à 15
# Notions abordées : les listes.

# Dans cet exercice, on continue avec des opérations assez simples utilisant les bases du langage Python.

# Le but ici est de créer une liste de nombres allant de 5 à 15 en utilisant une fonction de base de Python.

# Pour valider l'exercice, vous devez afficher cette liste, en utilisant la fonction print.


# SOLUTION
mon_range = range(5, 16)
ma_liste = list(mon_range)
print(ma_liste)


# EXPLICATION
# La fonction range permet de générer une liste de nombres rapidement.
# Depuis Python 3, il faut utiliser la fonction list pour convertir le résultat de la fonction range en liste.

