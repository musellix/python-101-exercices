
# 024 - Trouver l'erreur de module
# Notions abordées : les modules.

# Nous passons maintenant avec un exercice simple sur les modules.

# Le script actuel ne fonctionne pas et vous retournera une erreur. À vous de trouver où se situe l'erreur afin que le script fonctionne.

# Votre script doit au final retourner un nombre aléatoire compris entre 0 et 5.

# import random

# nombre_aleatoire = randint(0, 5)
# print(nombre_aleatoire)


# SOLUTION
import random
 
nombre_aleatoire = random.randint(0, 5)
print(nombre_aleatoire)


# EXPLICATION
# Pour utiliser une fonction à l'intérieur d'un module, il ne faut pas oublier de préfixer la fonction par le nom du module.
# Pour importer une fonction à l'intérieur d'un module directement dans l'espace global de notre script, on peut utiliser la syntaxe from module import fonction .
