# dans cet exercice, on va lire un fichier texte
# o va recuperer False, mais ca vaudra True
# A vous de trouver pourquoi

import os

cur_dir = os.path.realpath(os.path.dirname(__file__))
fichier = os.path.join(cur_dir, "fichier.txt")

with open(fichier, "r") as f:
    variable = f.read()

print(variable)
if variable:
    print("La variable est un boolean True")


# SOLUTION
print(type(variable))  # --> str

# à partir de Python 3.12, distutils a été supprimé de la bibliothèque standard
vrai_variable = distutils.util.strtobool(variable)
# utiliser une methode maison
def str_to_bool(s):
    return s.lower() == "true"


# EXPLICATION