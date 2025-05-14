# Alors dans cet exercice, j'ai caché un fichier sur mon ordinateur à l'intérieur d'un dossier.
# Et le but ça va être grâce à un script.
# De trouver ce fichier et de nous afficher le dossier dans lequel il est contenu.


# SOLUTION
import os

dossier_depart = "D:/projets/"
fichier_a_trouver = "fichier_a_trouver.txt"

for racine, dossiers, fichiers in os.walk(dossier_depart):
    if fichier_a_trouver in fichiers:
        print(os.path.join(racine, fichier_a_trouver))


# EXPLICATION
# os.walk : Cette fonction génère les noms de fichiers dans un répertoire en parcourant l'arborescence des dossiers
# Elle retourne un tuple (racine, dossiers, fichiers) pour chaque répertoire visité
