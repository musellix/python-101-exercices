# 052 - Créer un dictionnaire avec les lettres de l'alphabet
# Notions abordées : les dictionnaires.

# On continue avec les dictionnaires : dans cet exercice, vous devez créer un dictionnaire qui contient toutes les lettres de l'alphabet.

# La clé de chaque élément du dictionnaire doit contenir la position de la lettre dans l'alphabet, et la valeur doit être égale à la lettre en question.

# L'indice de la première lettre doit être 1 et non 0 !

# Votre dictionnaire doit donc être comme ci-dessous :

# {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'} 

# Aller plus loin : Essayez de faire tenir votre script en une seule ligne !


# SOLUTION
import string
alphabet = string.ascii_lowercase
dictionnaire = {}

for indice, lettre in enumerate(alphabet):
    dictionnaire[indice+1] = lettre
    
print(dictionnaire)

# ------------------

import string
alphabet = string.ascii_lowercase

#  on créé une liste qui contient les nombres de 1 à la longueur de l'alphabet
indices = range(1, len(alphabet) + 1)

#  on utilise la fonction zip, qui permet de créer une liste de tuples à partir de deux listes (la liste de nombres et les lettres de l'alphabet)
liste_zip = zip(indices, alphabet)

# la fonction dict pour convertir cette liste de tuple en dictionnaire
resultat = dict(liste_zip)
 
print(resultat)


# EXPLICATION
# Pour créer une liste de tuple à partir de deux listes, on utilise la fonction zip.
# Pour créer un dictionnaire à partir d'une liste de tuple, on peut utiliser la fonction dict.
