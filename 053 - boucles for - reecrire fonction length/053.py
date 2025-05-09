
# 053 - Recréer la fonction len
# Notions abordées : la boucle for, les fonctions.

# Un exercice toujours très intéressant à faire en Python est d'essayer de recréer les fonctions de base.

# Dans cet exercice, nous allons recréer la fonction len qui permet de compter la longueur d'une variable.

# Dans cet exemple, nous voulons compter le nombre de lettres dans le mot 'bonjour'.

# Votre script doit donc retourner le nombre 7.


# SOlUTION
def longueur(variable):
    compte = 0
    for _ in variable:
        compte += 1
    return compte
 
print(longueur("bonjour"))


# EXPLICATION
# Pour boucler à travers les différents éléments de plusieurs types de variables, on peut utiliser une boucle for.
# Pour incrémenter facilement un nombre entier, on peut utiliser la syntaxe +=
