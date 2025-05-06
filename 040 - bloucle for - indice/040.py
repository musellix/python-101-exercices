
# 040 - Trouver l'erreur dans une boucle for
# Notions abordées : boucle for.

# On continue avec les boucles, cette fois-ci la boucle for.

# Le but de cet exercice est de printer l'index de chaque lettre du mot 'Python'.
# mot = "Python"

# for i in range(mot):
# 	print(i)

# Votre script doit donc retourner :

# 0
# 1
# 2
# 3
# 4
# 5
# Aller plus loin : En plus d'afficher l'index de chaque lettre, faites un print de la lettre de l'itération courante en plus.


# SOLUTION
mot = "Python"
for indice, valeur in enumerate(mot):
	print(indice)

# ---------------

mot = "Python"
for i in range(len(mot)):
    print(i)


# EXPLICATION
# Pour calculer la longueur d'une chaîne de caractère, on utilise la fonction len.