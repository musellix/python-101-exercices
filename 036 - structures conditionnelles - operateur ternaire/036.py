# 036 - Tester une condition sur une seule ligne
# Notions abordées : structures conditionnelles.

# Le but de cet exercice est de tester si quelqu'un est majeur ou non à l'aide d'un opérateur ternaire.

# Votre condition doit donc tenir sur une seule ligne pour être valide !

# Pour valider l'exercice, votre script doit donc contenir uniquement deux lignes : la ligne de déclaration de la variable, et la ligne pour l'opérateur ternaire.

# Si vous mettez une ligne de plus, même vide, l'exercice ne sera pas validé.

# Dans ce cas-ci, a est égal à 20, votre script devra donc printer 'Vous êtes majeur !'.


# SOLUTION
a = 20
majeur = print("Vous êtes majeur !") if a >= 18 else print("Vous êtes mineur")


# EXPLICATION
# operateur ternaire
# variable = expression if condition else expression

# Pour réaliser une structure conditionnelle sur une seule ligne, on utilise un opérateur ternaire.
