# Dans cet exercice
# Le but, ça va être d'écrire du texte à l'intérieur d'un fichier.


# SOLUTION

import os

chemin_script = os.path.dirname(__file__)
chemin = os.path.join(chemin_script, "fichier.txt")

with open(chemin, "a") as f:
    f.write("Bonjour !\n")
    f.write("Comment ça va ?\n")
    f.write("Au revoir !\n")    

