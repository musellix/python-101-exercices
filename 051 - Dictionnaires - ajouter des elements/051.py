# 051 - Ajouter des éléments à un dictionnaire
# Notions abordées : les dictionnaires, boucle for.

# On s'attaque maintenant aux dictionnaires, toujours avec un peu de boucle for pour pimenter le tout.

# Dans cet exercice, vous devez boucler à travers la liste et ajouter au dictionnaire employes seulement les éléments de la liste qui sont des chaînes de caractères.

# Le but de l'exercice est de trier les données et de construire un dictionnaire d'employés.

# Les clés du dictionnaire doivent être 'id-xx', xx étant le numéro de l'employé.

# employes = {}
# liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]

# Votre script devra donc retourner le dictionnaire suivant :
# {'id-01': 'Pierre', 'id-02': 'Marie', 'id-03': 'Adrien'} 


# SOLUTION
employes = {}
liste = [10, 2329, 5, "Pierre", 203, "Marie", 867, "Adrien"]
i = 1
 
for element in liste:
    if not str(element).isdigit():
        employes["id-{:02d}".format(i)] = element
        i += 1
 
print(employes)


# EXPLICATION
# Pour vérifier si une chaîne de caractère ne contient que des nombres, on utilise la fonction isdigit.
# Pour formater un nombre pour qu'il contienne toujours 2 chiffres, on utilise la syntaxe 02d à l'intérieur d'accolades utilisées pour la fonction format.
