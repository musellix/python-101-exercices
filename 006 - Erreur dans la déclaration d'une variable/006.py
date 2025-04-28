# Notions abordées : les variables.


# ENONCE
# Le but de cet exercice est de trouver et réparer l'erreur présente dans le code.

# Vous devez modifier le code dans la console afin de ne plus avoir d'erreurs lors de l'exécution du script.

# Vous ne devez pas toucher à la fonction print, juste la déclaration des variables.

# list = range(3)
# list2 = range(5)
# print(list(list2))


# SOLUTION
list1 = range(3)
list2 = range(5)
print(list(list2))


# EXPLICATION
# Le problème qui survient dans le script de départ vient du fait que nous assignons 'range(3)' dans une variable qui est déjà utilisée par Python pour convertir un objet en liste (la fonction list).
