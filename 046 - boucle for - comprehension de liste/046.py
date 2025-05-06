# 046 - Récupérer seulement les éléments pairs d'une liste avec une compréhension de liste
# Notions abordées : boucle for, structure conditionnelle, compréhension de liste.

# On continue avec le même exercice qui consiste à récupérer seulement les nombres pairs d'une liste.

# Cette fois-ci, nous allons effectuer le même code que précédemment mais en une seule ligne, grâce aux compréhensions de liste.
# nombres = range(50)

# Votre script, pour être validé, doit donc tenir en 3 lignes : une ligne pour déclarer la liste, une ligne pour la trier, et une dernière ligne pour afficher la liste.


# SOLUTION
nombres = range(50)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)


# EXPLICATION
# Pour exécuter une boucle for sur une seule ligne et ainsi trier les éléments d'une liste, on utilise une compréhension de liste.
