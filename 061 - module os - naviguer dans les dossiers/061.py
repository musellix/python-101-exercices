# 061 - Créer une fonction pour remonter dans une structure de dossiers
# Notions abordées : le module os, la boucle while, les fonctions.

# Dans cet exercice, nous abordons le module os !

# Le but de cet exercice est de créer une fonction, qui permette de remonter dans une structure de dossier autant de fois qu'indiqué.

# Par exemple avec le dossier suivant : /Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy 

# Nous allons indiquer à la fonction 'remonter_dossier' le nombre de dossier que l'on veut remonter, par exemple :

# remonter_dossier("/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy", 3) 

# Notre fonction va donc remonter dans la structure de dossier 3 fois et nous retourner le chemin suivant :

# /Users/Thibh/Desktop 


# SOLUTION
import os

def remonter_dossier(chemin, nb):
    for _ in range(nb):
        chemin = os.path.dirname(chemin)
    return chemin


dossier = "/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy"
print(remonter_dossier(dossier, 3))

# --------------------------

import os
 
dossier = "/Users/Thibh/Desktop/Dossier_01/Tutoriel/Udemy"
 
def remonter_dossier(dossier, iterations=1):
    i = 0
    while i < iterations:
        dossier = os.path.dirname(dossier)
        i += 1
 
    return dossier
 
print(remonter_dossier(dossier, 3))


# EXPLICATION
# Pour récupérer le dossier parent d'un fichier ou d'un dossier, on utilise la fonction os.path.dirname du module os.path.