# Notions abordées : la fonction print.

# ENONCE
# Dans cet exercice, nous allons utiliser les nouvelles fonctionnalités de Python 3, afin de printer les 3 variables a, b et c, séparées par un symbole d'addition (+).

# Votre script doit donc afficher : 2 + 6 + 3.

# a = 2
# b = 6
# c = 3
# print(a, b, c)


# SOLUTION
a = 2
b = 6
c = 3

print(a, b, c, sep=' + ')


# EXPLICATION
# Depuis la version 3 de Python, la fonction print accepte un paramètre 'sep' qui permet de séparer les éléments que l'on print par une chaîne de caractère.