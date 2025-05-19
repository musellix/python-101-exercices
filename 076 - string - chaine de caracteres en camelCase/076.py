
# 076 - Convertir une chaîne de caractère en camelCase
# Notions abordées : les boucles, les chaînes de caractères.

# On continue avec les chaînes de caractères dans cet exercice dans lequel vous devez convertir une phrase en un mot au format camelCase.

# Le camelCase est une façon de formater une suite de mots pour que chaque mot soit séparé par une majuscule, excepté le premier mot.

# Dans ce cas-ci, votre script doit donc convertir la phrase 'Phrase en camel case' en 'phraseEnCamelCase'.


# SOLUTION
phrase = "Phrase en camel case"
phrase = phrase.lower()
phrase = phrase.split()

retour = ""
for id, mot in enumerate(phrase):
    if id > 0:
        retour += mot.capitalize()
    else:
        retour += mot
print(retour)

# --------------------------

phrase = "Phrase en camel case"
phrase_split = phrase.split()
 
resultat = [phrase_split.pop(0).lower()]
 
for mot in phrase_split:
    resultat.append(mot.capitalize())
 
resultat_formate = "".join(resultat)
 
print(resultat_formate)


# EXPLICATION
# Pour récupérer un élément dans une liste par son indice et l'enlever de cette même liste, on utilise la méthode pop.
# Pour convertir une chaîne de caractère en minuscule, on utilise la méthode lower.
# Pour convertir une chaîne de caractère en mot commençant par une majuscule, on utilise la méthode capitalize.
# Pour joindre ensemble tous les éléments d'une liste ensemble par un caractère, on utilise la méthode join.
