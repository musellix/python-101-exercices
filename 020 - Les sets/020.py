# 020 - Récupérer les éléments communs à deux listes
# Notions abordées : les sets.

# Dans cet exercice, vous allez devoir récupérer les éléments communs aux deux listes.

# Dans ce cas-ci, votre liste commune devra contenir les nombres 5, 7, et 10.

# Vous pouvez utiliser les sets pour cet exercice.

# Pour aller plus loin : Essayez de faire cet exercice sans utiliser les sets.

# liste_01 = [1, 5, 6, 7, 9, 10, 11]
# liste_02 = [2, 3, 5, 7, 8, 10, 12]


# SOLUTION
liste_01 = [1, 5, 6, 7, 9, 10, 11]
liste_02 = [2, 3, 5, 7, 8, 10, 12]

set_01 = set(liste_01)      # {1, 5, 6, 7, 9, 10, 11}
set_02 = set(liste_02)      # {2, 3, 5, 7, 8, 10, 12}

print(set_01 & set_02)              # {5, 7, 10}
print(set_01.intersection(set_02))  # {5, 7, 10}


# EXPLICATION
# Pour convertir une liste en set, on utilise la fonction set.
# Pour récupérer les éléments communs à deux set, on utilise la méthode intersection.

