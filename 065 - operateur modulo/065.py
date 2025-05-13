
# 065 - Trouvez tous les diviseurs d'un nombre
# Notions abordées : les boucles, les opérateurs mathématiques.

# Dans cet exercice, nous cherchons tous les diviseurs d'un nombre, dans ce cas-ci, le nombre 50.

# Les diviseurs du nombre 50 correspondent à tous les nombres par lesquels on peut diviser 50 sans qu'il n'y ait de reste à la division.

# Par exemple, 25 est un diviseur de 50 (car 50 / 25 = 2, et il reste 0).


# SOLUTION
nombre = 50
diviseurs = []

for val in range(1, nombre + 1):
    if nombre % val == 0:
        diviseurs.append(val)

print(diviseurs)

# ------------------------------

nombre = 50
liste_nombres = list(range(1, nombre+1))
diviseurs = []
 
for i in liste_nombres:
    if nombre % i == 0:
        diviseurs.append(i)
 
print(diviseurs)


# EXPLICATION
# Pour récupérer le reste de la division d'un nombre par un autre, on utilise l'opérateur modulo (%).
