# Alors dans cet exercice.
# Le but, ça va être de transformer un chemin relatif en chemin absolu.
# sans passer par le module path

# l'equivalent de 
# import os
# chemin = "/Users/Thibh/Desktop/Dossier_01/../Dossier_02/Udemy"
# print(os.path.normpath(chemin))


# SOLUTION
def chemin_absolu(chemin):
    pass
    chemin = chemin.split("/")

    for dossier in chemin:
        if dossier == "..":
            chemin.remove(dossier)
            chemin.remove(chemin[-1])
        elif dossier == ".":
            chemin.remove(dossier)
        elif dossier == "":
            chemin.remove(dossier)

    chemin = "/".join(chemin)
    return chemin


chemin = "/Users/Thibh/Desktop/Dossier_01/../Dossier_02/Udemy"
print(chemin_absolu(chemin))

# --------------------------

import os
chemin = "/Users/Thibh/Desktop/Dossier_01/../Dossier_02/Udemy"
 
def normalize_path(chemin):
    chemin_parts = chemin.split("/")
    while ".." in chemin_parts:
        index = chemin_parts.index("..")
        chemin_parts.pop(index)
        chemin_parts.pop(index-1)
 
    return os.sep.join(chemin_parts)
 
a = normalize_path(chemin)


# EXPLICATION

