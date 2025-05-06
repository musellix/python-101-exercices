# 045 - Récupérer seulement les éléments pairs d'une liste
# Notions abordées : boucle for, structure conditionnelle.

# Dans cet exercice, nous avons une liste qui contient 50 nombres.

# Le but de cet exercice est de récupérer dans une seconde liste, la liste nombres_pairs, uniquement les nombres pairs de la première liste.
# nombres = range(50)
# nombres_pairs = []

# Votre script doit donc afficher la liste suivante :
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48] 


# SOLUTION
nombres = range(50)
nombres_pairs = []
 
for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)
 
print(nombres_pairs)

# ---------------

nombres = range(50)
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)


# EXPLICATION
# Pour vérifier si un nombre est pair, on utilise l'opérateur mathématique modulo, en vérifiant si le modulo de notre nombre par 2 est égal ou non à 0.
