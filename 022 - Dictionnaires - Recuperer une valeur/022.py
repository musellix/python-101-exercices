# 022 - Récupérer une valeur dans un dictionnaire
# Notions abordées : les dictionnaires.

# Dans cet exercice, nous allons récupérer la valeur de la clé 'prenom', contenue dans le dictionnaire employes.

# Votre script doit donc retourner la chaîne de caractères 'Pierre'.

# Aller plus loin : construisez votre script de sorte qu’il ne produise aucune erreur si les clés du dictionnaire venaient à être modifiées.


# SOLUTION
employes = {"01": {"identite": {"prenom": "Pierre", "nom": "Dupont"}}}
print(employes.get("01", {}).get("identite", {}).get("prenom", "valeur inconnue"))


# EXPLICATION
# Pour récupérer la valeur associée à une clé dans un dictionnaire, on peut utiliser la fonction get, qui permet de spécifier une valeur par défaut à retourner si la clé n'est pas trouvée.




