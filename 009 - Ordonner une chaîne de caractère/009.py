# 009 - Ordonner une chaîne de caractère
# Notions abordées : les chaînes de caractères.


# ENONCE
# Le but de cet exercice et de remettre en ordre alphabétique les prénoms présents dans la chaîne de caractères.

# Vous devez donc afficher à la fin de l'exercice, la chaîne de caractères suivante :

# Anne, Julien, Lucien, Marie, Pierre

# Attention, les espaces sont importants si vous voulez valider l'exercice !


# SOLUTION
chaine = "Pierre, Julien, Anne, Marie, Lucien"
chaine_liste = chaine.split(", ")
chaine_liste.sort()
chaine_en_ordre = ", ".join(chaine_liste)
print(chaine_en_ordre)


# EXPLICATION
# Tout d'abord, il faut séparer les différents prénoms de la chaîne de caractère pour les mettre dans une liste.

# En effet, on ne peut pas trier une chaîne de caractère, il va donc falloir passer par une liste.

# Pour séparer les différents prénoms, on utilise la fonction split, qui permet de séparer la chaîne de caractère en plusieurs éléments, en opérant la séparation sur la virgule. Vous noterez qu'on a ajouté un espace après la virgule pour ne pas récupérer l'espace dans les prénoms de notre liste.

# À ce stade-ci, nous avons donc la liste suivante :

# ['Pierre', 'Julien', 'Anne', 'Marie', 'Lucien'] 

# Il faut maintenant ordonner cette liste, ce que nous faisons à la ligne suivante avec la fonction sort.

# chaine_liste.sort() 

# Il ne reste plus qu'à joindre de nouveaux les prénoms de la liste avec le caractère que nous avons utilisé précédemment pour réaliser la séparation (une virgule suivie d'un espace). Pour cela, nous utilisons la méthode join.

# chaine_en_ordre = ", ".join(chaine_liste) 

# POINTS IMPORTANTS À RETENIR
# On ne peut pas trier une chaîne de caractère.
# Pour séparer une chaîne de caractère en plusieurs éléments, on utilise la fonction split.
# Pour trier une liste, on utilise la fonction sort.
# Pour joindre différents éléments d'une liste par une chaîne de caractère, on utilise la méthode join.