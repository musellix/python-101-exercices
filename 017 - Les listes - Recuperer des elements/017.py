# 017 - Récupérer des éléments dans une liste
# Notions abordées : les listes.

# On monte d'un cran dans cet exercice, dans lequel vous devez récupérer plusieurs éléments de la liste.

# Pour réussir cet exercice, vous devez afficher le premier élément ('Pierre'), le dernier élément ('Marie'), les deux premiers éléments (['Pierre', 'Paul']) et les deux derniers éléments (['Paul', 'Marie']) avec la fonction print.

# ma_liste = ["Pierre", "Paul", "Marie"]


# SOLUTION
ma_liste = ["Pierre", "Paul", "Marie"]

# le 1er element
print(ma_liste[0])

# le dernier element
print(ma_liste[-1])

# les 2 premiers elements
print(ma_liste[0:2])

# les 2 derniers elements
print(ma_liste[-2:])



# EXPLICATION
# Pour récupérer plusieurs éléments à l'intérieur d'une liste, on utilise le slicing : ma_liste[début:fin]
# Pour récupérer des éléments en partant de la fin, on peut utiliser des indices négatifs.
