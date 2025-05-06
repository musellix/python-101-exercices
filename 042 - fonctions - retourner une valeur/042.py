
# 042 - Trouver l'erreur dans la fonction
# Notions abordées : les fonctions.

# On continue avec les erreurs à trouver dans les fonctions !

# Cette fois-ci, le script ne retourne pas d'erreur mais n'affiche pas le résultat escompté.

# Modifiez la fonction pour que le print de resultat affiche le résultat de l'addition.

# def addition(a, b):
# 	c = a + b


# resultat = addition(5, 10)
# print(resultat)


# SOLUTION
def addition(a, b):
    c = a + b
    return c
 
resultat = addition(5, 10)
print(resultat)


# EXPLICATION
# Pour retourner une valeur à l'intérieur d'une fonction, on utilise le mot clé return.
