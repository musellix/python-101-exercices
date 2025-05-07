# 049 - Enlever les doublons d'une liste
# Notions abordées : boucle for.

# Le but de cet exercice est d'enlever les doublons de la liste.
# nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

# Pour réussir l'exercice, vous devez utiliser une autre méthode que celle qui consiste à convertir la liste en set pour enlever les doublons.

# Votre script doit donc afficher la liste suivante :
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 


# SOLUTION
nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
nombres_set = set(nombres)
nombres_uniques = list(nombres_set)
print(nombres_uniques)

# ---------------

nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
nombres_sans_duplicats = []
 
for i in nombres:
    if i not in nombres_sans_duplicats:
        nombres_sans_duplicats.append(i)
 
print(nombres_sans_duplicats)


# EXPLICATION
# Pour vérifier si un élément est déjà présent ou non dans une liste, on utilise la syntaxe i in liste. Si le nombre est déjà dans la liste, cette syntaxe retournera True, si non, False.
