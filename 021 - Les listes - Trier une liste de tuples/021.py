# 021 - Trier une liste de tuples
# Notions abordées : les listes, les tuples.

# Dans cet exercice, l'objectif est de trier une liste qui contient des tuples :

# liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)] 

# Comme vous pouvez le voir, la liste contient des tuples qui ont comme premier élément le nom d'un film, et comme deuxième élément leur note sur 5.

# Le but de l'exercice est de trier ces tuples en fonction de la note qui leur a été attribuée.

# Votre script doit donc retourner la liste suivante :
# [('Wall-E', 3), ('Blade Runner', 4), ('Harry Potter', 5)] 


# liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]

# # Trier la liste ici

# print(liste)


# SOLUTION
liste = [("Harry Potter", 5), ("Wall-E", 3), ("Blade Runner", 4)]
liste.sort(key=lambda x: x[1])
print(liste)


# EXPLICATION
# La fonction sort accepte un argument 'key', auquel nous pouvons passer une fonction lambda pour trier une liste selon des critères spécifiques.

