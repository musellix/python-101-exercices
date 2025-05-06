
# 047 - Additionner les chiffres d'un nombre
# Notions abordées : boucle for.

# Le but de cet exercice est de calculer la somme de chaque chiffre d'un nombre.
# nombre = 209812
# Dans ce cas-ci, votre script doit retourner le nombre 22 (2 + 0 + 9 + 8 + 1 + 2).

# Aller plus loin : Essayez de faire tenir votre script en une seule ligne, grâce aux compréhensions de liste.


# SOLUTION
nombre = 209812
somme = sum([int(i) for i in str(nombre)])
print(somme)


# EXPLICATION
# Pour boucler sur chaque chiffre d'un nombre, on convertit le nombre en chaîne de caractère.
# Pour additionner ensemble tous les nombres contenus dans une liste, on utilise la fonction sum.
