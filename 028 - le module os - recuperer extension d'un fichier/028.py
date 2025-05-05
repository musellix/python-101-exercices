# 028 - Récupérer l'extension d'un fichier
# Notions abordées : le module os.

# Le but de cet exercice est de récupérer l'extension d'un fichier à l'aide du module os.

# Dans ce cas-ci, vous devez récupérer l'extension du fichier python.exe.

# Votre script doit retourner l'extension sans le point. Vous devez donc récupérer la chaîne de caractères 'exe'.


# SOLUTION
import os

fichier = "C:/Python36/python.exe"
extension_avec_point = os.path.splitext(fichier)[1]
extension_sans_point = extension_avec_point[1:]

print(extension_sans_point)


# EXPLICATION
# Pour manipuler des chemins de dossier, on utilise le module os.path.
# Pour séparer un chemin de son extension, on utilise la fonction os.path.splitext.
