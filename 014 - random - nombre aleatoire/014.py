# 014 - Créer un générateur de lancer de dés
# Notions abordées : les modules, la boucle for.

# Le but de cet exercice est de générer 6 lancer de dés aléatoires, allant de 1 à 6.

# Votre script devra donc par exemple retourner les lancer suivants :

# 1
# 4
# 5
# 2
# 2
# 6


# SOLUTION
import random
 
for _ in range(6):
    nombre = random.choice(range(1, 7))
    # nombre = random.randint(1, 6)
    print(nombre)


# EXPLICATION
# Pour récupérer un élément aléatoire dans une liste, on utilise la fonction choice du module random.
