# 023 - Additionner les valeurs d'un dictionnaire
# Notions abordées : les dictionnaires.

# On continue avec les dictionnaires ! Dans cet exercice, vous devez additionner toutes les valeurs du dictionnaire ensemble.

# Votre script doit donc retourner le nombre 8700.

# Aller plus loin : Essayez de faire tenir votre script en une seule ligne :)


# SOLUTION
employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
sum = 0

for cle, valeur in employes.items():
  sum = sum + valeur
  
print(sum)

# --------------

employes = {"Pierre": 2500, "Marie": 5000, "Julien": 1200}
print(sum(employes.values()))


# EXPLICATION
# Pour récupérer toutes les valeurs d'un dictionnaire, on utilise la méthode values.
# Pour faire la somme de plusieurs nombres, on utilise la fonction sum.

