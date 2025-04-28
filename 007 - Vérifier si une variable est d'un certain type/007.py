# 007 - Vérifier si une variable est d'un certain type
# Notions abordées : les variables.


# ENONCE
# Dans cet exercice, vous allez devoir vérifier que la variable 'prenom' est bien une chaîne de caractères.

# La variable prenom est définie au début du script par une chaîne de caractère.

# Votre script doit donc printer une première fois la phrase "La variable est une chaîne de caractères".

# La variable prenom est ensuite redéfinie et assignée au nombre 0.

# Vous devez donc tester de nouveau votre condition mais cette fois-ci, votre script ne doit pas printer la phrase.


# SOLUTION
prenom = "Pierre"
 
if type(prenom) == str:
    print("La variable est une chaîne de caractères")
 
prenom = 0
 
if isinstance(prenom, str):
    print("La variable est une chaîne de caractères")


# EXPLICATION

# Pour vérifier si une variable est d'un certain type, on peut utiliser la fonction type ou la fonction isinstance.
