# 034 - Mélanger les lettres d'un mot
# Notions abordées : le module random.

# Dans cet exercice, nous allons mélanger les lettres d'un mot grâce au module random.

# Le mot résultant devra commencer par une majuscule. Dans cet exercice nous allons mélanger le mot 'Bonjour'.

# Votre script devra mélanger les lettres de ce mot pour donner par exemple : 'Ojnoubr'.


# SOLUTION
import random

mot = "Bonjour"

liste = list(mot)
random.shuffle(liste)
mot = "".join(liste).capitalize()

print(mot)


# EXPLICATION
# Pour mélanger les éléments d'une liste, on utilise la fonction shuffle du module random.
# Pour convertir une chaîne de caractères en liste, on utilise la fonction list.
