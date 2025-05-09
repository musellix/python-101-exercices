
# 055 - Créer une pyramide de symboles
# Notions abordées : les boucles, les chaînes de caractères.

# Dans cet exercice, nous allons, à partir d'une variable symbole et une variable taille créer une pyramide avec ce symbole, de la hauteur du nombre contenu dans la variable taille.

# Dans cet exemple-ci, nous allons donc afficher une pyramide de dollars ($) de hauteur 10.

# Votre script devra donc afficher :

#          $ 
#         $ $ 
#        $ $ $ 
#       $ $ $ $ 
#      $ $ $ $ $ 
#     $ $ $ $ $ $ 
#    $ $ $ $ $ $ $ 
#   $ $ $ $ $ $ $ $ 
#  $ $ $ $ $ $ $ $ $ 
# $ $ $ $ $ $ $ $ $ $
# L'éditeur de code d'Udemy n'étant pas très pratique pour afficher le résultat des print, je vous conseille de réaliser cet exercice en dehors d'Udemy, dans un éditeur de code tel que Visual Studio Code ou PyCharm et de vérifier votre code ici une fois que vous pensez qu'il est bon.


# SOLUTION
symbole = "$"
taille = 10

for i in range(1, taille + 1):
    symbs = ""
    
    for j in range(i):
        symbs += symbole
        if j < i:
            symbs += " "
            
    print(" " * (taille - j - 1) + symbs)

# ----------------------------

symbole = "$"
taille = 10
 
for i in range(1, taille + 1):
    espaces = " " * (taille - i)
    print(espaces + (symbole + " ") * i)


# EXPLICATION
# Pour afficher plusieurs fois de suite un caractère, on peut tout simplement multiplier une chaîne de caractère par un nombre.
