
# 044 - Récupérer l'indice de l'itération dans une boucle
# Notions abordées : boucle for.

# Les boucles for, encore et toujours, avec cette fois-ci, un exercice dans lequel nous allons récupérer à la fois l'indice et l'élément sur lequel nous bouclons dans chaque itération de la boucle for.
# liste = ["Pierre", "Paul", "Marie"]

# Votre script doit donc retourner dans ce cas-ci :

# 0 Pierre
# 1 Paul
# 2 Marie


# SOLUTION
liste = ["Pierre", "Paul", "Marie"]

for indice, valeur in enumerate(liste):
    print(f"{indice} {valeur}")


# EXPLICATION
# Pour récupérer un élément et son indice dans une boucle for, on utilise la fonction enumerate.
