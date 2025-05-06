
# 038 - Trier trois nombres sans condition
# Notions abordées : fonctions de base.

# Dans cet exercice, nous allons trier trois nombres sans avoir recours à l'utilisation de structures conditionnelles ni à la méthode sort.

# À l'aide des fonctions de base de Python, vous allez donc devoir trouver un moyen de trier les variables a, b et c du plus petit au plus grand.
# a = 4
# b = 6
# c = 2
# Dans le cas de cet exercice, avec a = 4, b = 6 et c = 2, votre script doit printer : 'Les nombres dans l'ordre sont 2, 4 et 6'.



# SOLUTION
a = 4
b = 6
c = 2

mini = min(a, b, c)
maxi = max(a, b, c)
moyen = a + b + c - mini - maxi     # juste des maths de base

print(f"Les nombres dans l'ordre sont {mini}, {moyen} et {maxi}")


# EXPLICATION
# Pour trouver la valeur maximale ou minimale entre plusieurs variables, on utilise les fonctions min et max.

