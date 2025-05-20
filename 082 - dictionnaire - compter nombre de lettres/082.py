# 082 - Compter le nombre d'occurrence de chaque lettre de l'alphabet dans un texte
# Notions abordées : les boucles, les dictionnaires.

# Dans cet exercice, nous cherchons à analyser un texte pour savoir combien de fois on y retrouve chaque lettre de l'alphabet.

# Nous avons donc un texte classique de Lorem Ipsum et votre script doit retourner un dictionnaire avec chaque lettre de l'alphabet et le nombre de fois qu'elle apparaît dans le texte.

# Dans l'exemple ci-dessous, votre script devra retourner le dictionnaire suivant :

# {'a': 29, 'b': 3, 'c': 16, 'd': 19, 'e': 38, 'f': 3, 'g': 3, 'h': 1, 'i': 42, 'j': 0, 'k': 0, 'l': 22, 'm': 17, 'n': 24, 'o': 29, 'p': 11, 'q': 5, 'r': 22, 's': 18, 't': 32, 'u': 29, 'v': 3, 'w': 0, 'x': 3, 'y': 0, 'z': 0} 


# SOLUTION
import string 

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

alphabet = string.ascii_lowercase

compteur = {}
for lettre in alphabet:
    compteur[lettre] = 0

lorem = lorem.lower()

for lettre in lorem:
    if lettre in alphabet:
        compteur[lettre] += 1

print(compteur)

# ---------------------------

alphabet = string.ascii_lowercase
resultat = dict(zip(alphabet, [0] * len(alphabet)))
 
for lettre in lorem.lower():
    if resultat.get(lettre) is not None:
        resultat[lettre] += 1
 
print(dict(resultat))


# EXPLICATION
# Pour créer une liste de tuple à partir de deux listes, on utilise la fonction zip.
# Pour créer un dictionnaire à partir d'une liste de tuple, on utilise la fonction dict.
# Pour récupérer la valeur d'une clé dans un dictionnaire sans risquer de faire planter notre script si la clé n'existe pas, on utilise la méthode get.
