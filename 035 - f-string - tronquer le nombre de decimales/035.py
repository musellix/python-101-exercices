
# 035 - Tronquer le nombre de décimales
# Notions abordées : les f-string.

# Dans cet exercice, nous voulons tronquer le nombre de décimales contenues après la virgule dans la variable nombre, par le nombre contenu dans la variable decimales.

# Votre script doit donc afficher : 'Nombre tronqué: 2938.489'.

# Vous pouvez réaliser cette opération avec les f-string ou la méthode format.

# nombre = 2938.48872
# decimales = 3

# print("Nombre tronqué: ")


# SOLUTION
nombre = 2938.48872
decimales = 3
 
print(f"Nombre tronqué: {nombre:.{decimales}f}")
 
# Avec la méthode format
print("Nombre tronqué: {nombre:.{decimales}f}".format(nombre=nombre, decimales=decimales))

# Avec la methode round
solution = round(nombre, decimales)
print(f"Nombre tronqué: {solution}")


# EXPLICATION
# On peut tronquer directement un nombre pour n'afficher qu'une certaine partie des décimales après la virgule grâce aux f-string et la syntaxe {nombre:.3f}.

