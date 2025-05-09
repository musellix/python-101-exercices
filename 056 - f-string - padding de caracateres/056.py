
# 056 - Formater un texte avec la méthode format
# Notions abordées : les f-string.

# Dans cet exercice, nous continuons d'aborder le formatage de texte avec les f-string.

# Le but de cet exercice est d'afficher le texte suivant :

# -------------
# |     B     |
# |     o     |
# |     n     |
# |     j     |
# |     o     |
# |     u     |
# |     r     |
# |           |
# |     U     |
# |     d     |
# |     e     |
# |     m     |
# |     y     |
# -------------
# Vous devez afficher le texte 'Bonjour Udemy', entouré des symboles '-' et '|'.

# Votre script doit s'adapter à la longueur du texte. Le texte doit ainsi toujours être placé au milieu des symboles.



# SOLUTION

texte = "Bonjour Udemy"
largeur = 13
nb_espaces = int((largeur-3)/2)


print("-" * largeur)

for lettre in texte:
    print("|" + " " * nb_espaces + lettre + " " * nb_espaces + "|")

print("-" * largeur)

# --------------------------

texte = "Bonjour Udemy"
size = len(texte)
 
symbol = "-"
symbol2 = "|"
 
print(symbol * size)
 
for lettre in texte:
    print(f"{symbol2}{lettre:^{size - 2}}{symbol2}")

#     {lettre:^{size - 2}}
# On indique vouloir insérer l'objet contenu dans la variable lettre 

# Ensuite, avec les deux points et l'accent circonflexe, on signifie que l'on veut ajouter un 'padding' avant et après cette lettre : en gros, python va ajouter autant d'espaces que nécessaire avant et après la variable que l'on insère dans l'accolade, afin que le nombre total de caractère soit égal au nombre passé.
 
print(symbol * size)


# EXPLICATION

# Pour faire en sorte qu'une chaîne de caractères occupe un nombre précis de caractères, vous pouvez la 'padder' avec des espaces, en utilisant l'accent circonflexe à l'intérieur de votre f-string.