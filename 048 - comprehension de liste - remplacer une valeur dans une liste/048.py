# 048 - Remplacer un élément dans une liste
# Notions abordées : compréhension de liste.

# On continue avec l'utilisation des compréhensions de liste, cette fois-ci pour remplacer une chaîne de caractères dans les éléments d'une liste par une autre chaîne de caractères.

# Dans cet exemple, nous devons remplacer 'Julie' par 'Julien' dans tous les éléments de la liste.

# Votre script doit donc afficher la liste suivante :

# ['Pierre', 'Marie', 'Julien', 'Adrien', 'Julien'] 


# SOLUTION
liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"

new_liste = [nom.replace(nom_a_chercher, nouveau_nom) for nom in liste]
print(new_liste)


# EXPLICATION
# Pour remplacer un mot par un autre, on utilise la fonction replace.
