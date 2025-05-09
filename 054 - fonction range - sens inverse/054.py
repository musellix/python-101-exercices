# 054 - Créer un motif avec des print
# Notions abordées : la fonction print, la fonction range, la boucle for.

# Dans cet exercice, vous allez devoir afficher une moitié de losange composée du symbole * grâce à une boucle for et la fonction print.

# Votre script doit donc afficher le motif suivant :

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *
# Le nombre de symboles maximum affiché doit être de 8 (valeur contenue dans la variable n).


# SOLUTION
n = 8
symbole = "*"

nombres = list(range(1, n+1)) + list(range(n-1, 0, -1))
# -> [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]

for i in nombres:
    print(symbole*i)


# EXPLICATION
# Pour créer une liste avec la fonction range en sens inverse, on peut passer un troisième paramètre : -1

