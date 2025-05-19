
# 078 - Vérifier si une phrase est un palindrome
# Notions abordées : les chaînes de caractères.

# Dans cet exercice, nous allons vérifier si une phrase est un palindrome ou non. Un palindrome est un mot ou une phrase qui peut se lire de la même façon dans les deux sens.

# Dans cet exemple-ci, nous avons le palindrome 'Un roc cornu'. Votre script devra donc vérifier si cette phrase est un palindrome, et donc dans ce cas-ci, retourner la valeur True.

# Aller plus loin : Essayez cette fois-ci de ne pas utiliser la fonction reversed.


# SOLUTION
mot = "Un roc cornuaa"
mot = mot.lower()
mot = mot.replace(" ", "")

mot_reversed = mot[::-1]
# mot_reversed = ''.join(reversed(mot))

print(mot == mot_reversed)


# EXPLICATION
# Pour enlever tous les espaces d'une chaîne de caractère, on peut utiliser la méthode replace.
# Pour inverser une chaîne de caractère, on peut utiliser la syntaxe [::-1]
