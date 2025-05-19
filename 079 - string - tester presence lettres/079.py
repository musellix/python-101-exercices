# 079 - Vérifier si une phrase est un pangramme
# Notions abordées : les chaînes de caractères, les boucles.

# Encore un exercice avec un mot barbare que vous n'avez peut-être jamais entendu de votre vie. Un pangramme est une phrase qui contient toutes les lettres de l'alphabet au moins une fois.

# La phrase que nous utiliserons dans cet exercice est la suivante : "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre".

# Vous devez donc vérifier si cette phrase est bien un pangramme, et si c'est le cas, afficher la phrase : "La phrase est un Pangramme".


# SOLUTION
import string

phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"

lettres = string.ascii_letters

# Supprimer la ponctuation (pas necessaire en fait)
ponctuation = string.punctuation
# créer un tableau de traduction qui supprime tous les caractères de ponctuation
tableau_traduction = str.maketrans('', '', string.punctuation)
phrase = phrase.translate(tableau_traduction)

# supprimer les espaces
phrase = phrase.replace(" ","").lower()


liste_presence = [False] * 26

for lettre in phrase:
    if lettre in lettres:
        code_ascii = ord(lettre) - ord("a")
        liste_presence[code_ascii] = True

if all(liste_presence):
    print("La phrase est un Pangramme")

# -------------------------

import string
 
phrase = "Joyeux, ivre, fatigué, le nez qui pique, Clown Hary skie dans l’ombre"
phrase_lower = phrase.lower()
 
alphabet = list(string.ascii_lowercase)
 
for l in phrase_lower:
    if l in alphabet:
        alphabet.remove(l)
 
if alphabet:
    print("La phrase n'est pas un Pangramme")
else:
    print("La phrase est un Pangramme")


# EXPLICATION
# Pour récupérer toutes les lettres de l'alphabet, on utilise le module string et la constante "ascii_lowercase".
# Pour enlever un élément d'une liste, on utilise la méthode remove.
# Une liste vide est évaluée comme False.

