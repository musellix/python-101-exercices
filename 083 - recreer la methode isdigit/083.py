# 083 - Recréer la méthode isdigit
# Notions abordées : les fonctions, les boucles, les structures conditionnelles.

# Dans cet exercice, nous allons recréer une méthode appartenant aux chaînes de caractères, la méthode isdigit, qui permet de vérifier si une chaîne de caractères ne contient que des nombres.

# Nous allons transformer cette méthode en fonction.

# def isdigit(nombre):
#     pass

# print(isdigit("1854274"))

# À vous donc de combler la fonction isdigit afin de vérifier si la chaîne de caractères que l'on passe (ici "1854274") contient uniquement des nombres.
# Votre script doit dans ce cas-ci retourner True.

# Bien entendu, vous ne devez pas utiliser la méthode isdigit native de Python !

# Aller plus loin : vérifiez également si l'argument passé à la fonction est bien une chaîne de caractères afin d'éviter les erreurs (si par exemple l'utilisateur envoie une liste ou un boolean).


# SOLUTION
def isdigit(nombre):
    tous_les_chiffres = "0123456789"
    retour = True
    for chiffre in nombre:
        if chiffre not in tous_les_chiffres:
            retour = False
    return retour

print(isdigit("1854274"))

# --------------

def isdigit(variable):
    for i in variable:
        if i not in [str(n) for n in range(10)]:
	    return False
 
    return True
 
print(isdigit("1854274"))


# EXPLICATION
# Pour créer rapidement et efficacement des listes, on peut utiliser des compréhensions de liste et la fonction range.
# Pour vérifier si une variable est présente ou non dans une liste, on utilise "in" dans une condition : if variable in liste. La condition retournera True si la variable est présente dans la liste et False dans le cas contraire.
