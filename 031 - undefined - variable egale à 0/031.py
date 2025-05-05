# 031 - Trouver l'erreur : variable égale à 0
# Notions abordées : les structures conditionnelles, les nombres.

# Encore un exercice avec une syntaxe à corriger.

# Le script ci-dessous n'affichera pas la valeur de a. 

# Pourtant, la variable a n'est pas vide et contient bien un nombre.

# Modifiez la condition pour que le script affiche la valeur de la variable a.
# a = 0
# if a:
# 	print(a)


# SOLUTION
a = 0
if a is not None:
    print(a)


# EXPLICATION
# Le nombre 0 est équivalant au boolean False.
# Pour vérifier explicitement qu'une variable n'est pas égale à None, il vaut mieux utiliser la syntaxe if variable is not None.