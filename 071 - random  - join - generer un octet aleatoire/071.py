
# 071 - Générer un octet aléatoire
# Notions abordées : les modules, les boucles.

# Dans cet exercice, nous allons générer un octet aléatoire.

# Un octet est représenté par une suite de 8 chiffres allant de 0 à 1, par exemple : 01101110 qui est égal au nombre 110 en base décimale.

# Dans cet exercice, vous devez générer cet octet sous forme de chaîne de caractères (donc générer une chaîne de caractères qui contient 8 chiffres aléatoires de 0 à 1).

# Aller plus loin : Utilisez une compréhension de liste pour réduire le nombre de lignes dans votre code.


# SOLUTION
import random

nb = ""
for _ in range(8):
    nb += str(random.randint(0, 1))
    
print(nb)

# -----------------

import random
nb = "".join([str(random.randint(0, 1)) for _ in range(8)])    
print(nb)

# -----------------

import random
liste_random = [str(random.choice(range(2))) for _ in range(8)]
print("".join(liste_random))


# EXPLICATION
# Pour choisir un élément aléatoire entre plusieurs éléments dans une liste, on utilise la fonction choice du module random.
# Pour joindre plusieurs éléments d'une liste ensemble, on utilise la fonction join.
