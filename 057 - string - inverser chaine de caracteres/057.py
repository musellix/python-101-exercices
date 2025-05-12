# 057 - Ajouter un séparateur de milliers à un nombre
# Notions abordées : la boucle for, les fonctions, les structures conditionnelles.

# Dans cet exercice, nous voulons formater un nombre pour ajouter une virgule entre chaque millier.

# Ainsi, le nombre contenu dans la variable nombre devra être affiché comme ci-dessous :

# 52,039,480,394,023 

# Votre script doit bien entendue fonctionner peu importe le nombre.


# SOLUTION
nombre = 52039480394023
sNombre = str(nombre)
nombre = ""

for i, valeur in enumerate(sNombre[::-1]):
    if i > 0 and i % 3 == 0:
        nombre += ","
    nombre += valeur

nombre = nombre[::-1]

print(nombre)

# --------------------------

def ajout_separateur(nombre):
    nombre = str(nombre)[::-1]
    resultat = ""
 
    for i, chiffre in enumerate(nombre, 1):
        chiffre_formatte = chiffre + "," if i % 3 == 0 and i != len(nombre) else chiffre
        resultat += chiffre_formatte
 
    return resultat[::-1]
 
nombre = 52039480394023
print(ajout_separateur(nombre))


# EXPLICATION
# Pour inverser une chaîne de caractère, on peut utiliser la syntaxe [::-1]
# On peut passer un deuxième argument à la fonction enumerate pour commencer à un indice autre que 0.
# L'opérateur modulo permet de réaliser une opération tous les x itérations (car n % n est égal à 0).
