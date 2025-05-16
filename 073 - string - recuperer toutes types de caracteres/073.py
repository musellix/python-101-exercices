# 073 - Créer un générateur de mot de passe
# Notions abordées : le module string, le module random.

# Dans cet exercice, nous allons créer un générateur de mot de passe aléatoire.

# À l'aide du module string et du module random, vous allez devoir générer un mot de passe aléatoire de la longueur spécifiée dans la variable taille (ici, 8).

# Votre mot de passe doit pouvoir contenir des lettres minuscules, majuscules, n'importe quel chiffre de 0 à 9 et n'importe quel caractère spécial (!"#$%&' etc...).


# SOLUTION
import string
import random

taille = 8
characters = string.ascii_letters + string.digits + string.punctuation
mdp = ""

for _ in range(taille):
    mdp += random.choice(characters)
    
print(mdp)

# ----------------------

import string
import random
 
taille = 8
 
symboles = string.ascii_letters + string.digits + string.punctuation
mot_de_passe = ''.join(random.choice(symboles) for _ in range(taille))
 
print(mot_de_passe)


# EXPLICATION
# Pour récupérer toutes les lettres majuscules et minuscules de l'alphabet, on utilise la constante "ascii_letters" du module "string".
# Pour récupérer tous les nombres, on utilise la constante "digits" du module "string".
# Pour récupérer tous les symboles du clavier, on utilise la constante "punctuation" du module "string"
# Pour récupérer une lettre aléatoire dans une chaîne de caractère, on utilise la fonction "choice" du module "random".
