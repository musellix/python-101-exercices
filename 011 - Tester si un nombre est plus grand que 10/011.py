# 011 - Tester si un nombre est plus grand que 10
# Notions abordées : structures conditionnelles.

# Dans cet exercice, nous allons utiliser une structure conditionnelle pour vérifier si a est plus grand ou non que 10.

# Dans ce cas-ci, a est égal à 12, votre script devra donc afficher 'a est plus grand que 10'

# Aller plus loin : Vous pouvez également rajouter une condition pour tester si la variable a contient bien un nombre.


# SOLUTION
a = 12
if type(a) == int and a > 10:
    print("a est plus grand que 10")
elif a < 10:
    print("a est plus petit que 10")

# EXPLICATION
# Exercice très simple pour ceux d'entre vous qui sont habitués à Python.

# Il s'agissait ici de faire une structure conditionnelle de base afin de vérifier si le nombre a était plus grand ou plus petit que 10.

# Pour tester plusieurs conditions, on utilise la structure conditionnelle if, elif.
