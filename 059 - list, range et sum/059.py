# 059 - Calculer la somme des nombres entre deux nombres
# Notions abordées : la fonction sum, la fonction range.

# Dans cet exercice, nous allons calculer la somme des nombres entre deux nombres.

# Dans cet exemple-ci, nous prenons les nombres 2 et 6, le résultat de votre script doit donc être 20 (2 + 3 + 4 + 5 + 6).

# Attention : votre script doit fonctionner peu importe l'ordre dans lequel vous donnez les nombres : somme(2, 6) et somme(6, 2) doivent retourner le même résultat !


# SOLUTION
def somme(a, b):
    if a > b:
        liste = list(range(b, a+1))
    else:
        liste = list(range(a, b+1))

    return sum(liste)
		
print(somme(6, 2))

# --------------------------

def somme(a, b):
    return sum(range(min(a, b), max(a, b) + 1))
 
print(somme(2, 6))


# EXPLICATION
# La fonction range retourne une liste vide si le premier nombre est plus grand que le second.
# Pour récupérer le nombre le plus petit ou le plus grand entre plusieurs nombres, on utilise les fonctions min et max.
# La fonction sum permet d'additionner une liste de nombres.
