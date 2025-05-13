# 066 - Trouver les nombres divisibles par 7 mais qui ne sont pas des multiples de 3
# Notions abordées : les boucles, les opérateurs mathématiques, les structures conditionnelles

# Le but de cet exercice est de trouver tous les nombres de 0 à 1000 qui sont divisibles par 7 mais ne sont pas des multiples de 3.

# Par exemple, le nombre 14 est divisible par 7 (car 14 / 7 = 2, il reste 0), mais n'est pas un multiple de 3 (car 14 / 3 ne retourne pas un nombre entier).

# Pour valider l'exercice, vous devez récupérer tous ces nombres dans la liste nombres.


# SOLUTION
nombres = []

for val in range(1001):
    if val % 7 == 0 and val % 3 != 0:
        nombres.append(val)
        
print(nombres)


# EXPLICATION
# Pour vérifier si plusieurs conditions sont vraies, on utilise l'opérateur "and".
# Pour récupérer le reste d'une division, on utilise l'opérateur modulo (%).