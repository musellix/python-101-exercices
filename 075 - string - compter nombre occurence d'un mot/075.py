# 075 - Compter le nombre d'occurrence d'un mot dans un texte
# Notions abordées : les chaînes de caractères.

# Dans cet exercice, nous allons compter le nombre d'occurrences du mot 'elit' dans le texte en Lorem Ipsum contenu dans la variable lorem.
# lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# Dans cet extrait de texte, le mot apparaît une seule fois, votre script doit donc retourner le nombre 1.


# SOLUTION
import string

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

texte = 'elit'

# enver les signes de ponctuation
ponctuation = set(string.punctuation)
lorem = ''.join(caractere for caractere in lorem if caractere not in ponctuation)

loremList = lorem.split(" ")

nb = loremList.count(texte)
print(nb)

# ----------------------

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
 
mot = "elit"
 
lorem = lorem.replace(",", "").replace(".", "")
lorem = lorem.lower()
 
lorem_split = lorem.split()
print(lorem_split.count(mot))


# EXPLICATION
# Pour remplacer un caractère par un autre, ou l'effacer, on utilise la fonction replace.
# Pour convertir une chaîne de caractère en minuscule, on utilise la fonction lower.
# Pour séparer une chaîne de caractère sur les espaces, on utilise la fonction split.
# Pour compter le nombre d'occurrence d'un élément dans une liste, on utilise la fonction count.
