
# 084 - Recréer la méthode join
# Notions abordées : les fonctions.

# On continue avec les fonctions et méthodes de base que l'on essaie de comprendre et de recréer. Cette fois-ci, on s'intéresse à la méthode join qui permet de joindre plusieurs éléments d'une liste par une chaîne de caractères.

# Nous allons donc recréer cette méthode et la transformer en fonction. Votre fonction devra prendre comme premier argument l'élément avec lequel vous voulez séparer les éléments de votre liste.

# À la place d'une liste, nous passerons ici directement à la fonction des chaînes de caractères à joindre.

# Votre fonction devra donc être appelée de la façon suivante :

# join(":", "Bonjour", "tout", "le", "monde") 

# Et retournera la chaîne de caractère suivante :

# "Bonjour:tout:le:monde" 

# Votre fonction devra fonctionner avec autant de chaînes de caractères que voulu par l'utilisateur et bien entendu, interdit d'utiliser la méthode join !


# SOLUTION
def join(*args):
    retour = ''
    for i, arg in enumerate(args):
        if i > 1:
            retour += args[0]
        if i > 0:
            retour += arg
    return retour

j = join(":", "Bonjour", "tout", "le", "monde")
print(j)

# ----------------

def join(*args):
    resultat = ""
    
    separateur = args[0]
    elements = args[1:]
    
    for element in elements:
        resultat += element + separateur
 
    return resultat[:-1]
 
j = join(":", "Bonjour", "tout", "le", "monde")
print(j)


# EXPLICATION
# Pour envoyer et récupérer un nombre indéfini d'arguments à une fonction, on utilise *args.
# Pour récupérer tous les éléments d'une liste sauf le premier, on utilise la syntaxe de slice [1:]
# Pour récupérer tous les éléments d'une liste ou d'une chaîne de caractère sauf le dernier, on utilise la syntaxe de slice [:-1]
