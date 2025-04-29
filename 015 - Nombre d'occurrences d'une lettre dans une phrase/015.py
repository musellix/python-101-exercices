# 015 - Compter le nombre d'occurrences d'une lettre dans une phrase
# Notions abordées : les chaînes de caractères.

# Dans cet exercice, nous cherchons à compter le nombre d'occurrences d'une lettre dans une chaîne de caractères.

# Ici, nous cherchons le nombre de fois que la lettre "o" apparaît dans la phrase "Bonjour tout le monde".

# Votre script devra donc retourner dans ce cas-ci le nombre 4 !


# lettre_a_chercher = "o"
# phrase = "Bonjour tout le monde"


# SOLUTION
lettre_a_chercher = "o"
phrase = "Bonjour tout le monde"
print(phrase.lower().count(lettre_a_chercher))


# EXPLICATION
# Pour compter le nombre d'occurrences d'une lettre dans une chaîne de caractère, on utilise la fonction count.
# Pour convertir une chaîne de caractère en minuscule, on utilise la fonction lower.

