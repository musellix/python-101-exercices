# 026 - Importer une variable d'un autre module
# Notions abordées : les modules, les variables.

# Dans cet exercice, nous allons importer une variable d'un autre module dans notre script principal.

# Dans le fichier constants.py se trouve une variable nom qui contient le mot 'Udemy'.

# Le but de l'exercice est d'importer cette variable dans le fichier exercice.py pour l'afficher grâce à la fonction print.


# SOLUTION
import constants
print(constants.nom)


# EXPLICATION
# Pour importer une variable d'un module, il suffit d'importer le module dans lequel la variable est contenue.
