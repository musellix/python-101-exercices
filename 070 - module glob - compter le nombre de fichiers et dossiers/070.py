# Dans cet exercice
# Votre objectif
# Ça va être de compter le nombre de dossiers et de fichiers qui sont contenus à l'intérieur d'un dossier.

import os

dossier_parent = "D:/projets/python-101-exercices/"

nb = 0

for racine, dirs, fichiers in os.walk(dossier_parent):
    for dossier in dirs:
        nb += 1
    for fichier in fichiers:
        nb += 1

print(nb)

# -----------------------------

from glob import glob
 
dossier = "D:/projets/python-101-exercices/"
 
fichiers = glob(f"{dossier}/**", recursive=True)
print(len(fichiers))
