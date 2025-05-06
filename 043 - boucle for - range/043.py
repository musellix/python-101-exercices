# 043 - Afficher la table de multiplication d'un nombre
# Notions abordées : boucle for, fonction range.

# On continue avec la boucle for, cette fois-ci pour afficher la table de multiplication d'un nombre.

# Dans ce cas-ci, votre script doit afficher la table de multiplication du nombre 7 :

# 0 x 7 = 0
# 1 x 7 = 7
# 2 x 7 = 14
# 3 x 7 = 21
# 4 x 7 = 28
# 5 x 7 = 35
# 6 x 7 = 42
# 7 x 7 = 49
# 8 x 7 = 56
# 9 x 7 = 63
# 10 x 7 = 70
# Attention aux espaces entre chaque nombre et symbole !


# SOLUTION
nombre = 7

for indice in range(11):
    print(f"{indice} x {nombre} = {indice * nombre}")

# ---------------

nombre = 7
 
for i in range(11):
    print("{i} x {nombre} = {resultat}".format(i=i, nombre=nombre, resultat=i*nombre))


# EXPLICATION
# Il est possible de faire des opérations mathématiques directement à l'intérieur de la méthode format, afin d'insérer le résultat de ces opérations à l'intérieur d'une chaîne de caractère.