# 067 - Calculer la factorielle d'un nombre
# Notions abordées : les boucles.

# Dans cet exercice, nous cherchons la factorielle d'un nombre, dans ce cas-ci le nombre 5.

# La factorielle de 5 est égal à 120 (car 1 x 2 x 3 x 4 x 5 = 120).

# Votre script doit aussi gérer le cas dans lequel le nombre de départ est 0 (la factorielle de 0 est égale à 1).


# SOLUTION
nombre = 5
resultat = 1

for i in range(1, nombre + 1):
    resultat *= i
    
print(resultat)


# EXPLICATION
# Pour rapidement multiplier une variable par un nombre, on peut utiliser la syntaxe *=

