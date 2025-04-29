# 013 - Créer une liste de nombres pairs de 1 à 100
# Notions abordées : les listes.

# Dans cet exercice, on continue avec la fonction range, cette fois-ci pour créer une liste de nombres pairs allant de 1 à 100.

# Votre script doit afficher la liste, pensez-donc à faire un print à la fin. Si vous faites juste déclarer la liste, l'exercice ne sera pas validé.


# SOLUTION
mon_range = range(2, 101, 2)
ma_liste = list(mon_range)
print(ma_liste)


# EXPLICATION
# On peut spécifier un écart à la fonction range en passant un nombre en troisième argument.
