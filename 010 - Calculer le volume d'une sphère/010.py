# 010 - Calculer le volume d'une sphère
# Notions abordées : les opérateurs mathématiques.

# Dans cet exercice, nous allons calculer le volume d'une sphère ayant pour rayon 10 centimètres.

# La formule pour calculer le volume d'une sphère est :

# (4π/3) × rayon³

# rayon représentant la valeur du rayon (défini dans le code par la variable rayon).

# Pour réussir l'exercice, vous devez uniquement afficher le volume de la sphère, si vous rajoutez du texte en plus l'exercice ne sera pas validé (donc il suffit de laisser le print(volume) à la fin et de calculer le volume à la ligne d'avant).

# rayon = 10.0
# volume = 
# print(volume)


# SOLUTION
import math
rayon = 10.0
volume = (4.0 * math.pi / 3.0) * (rayon ** 3)
print(volume)


# EXPLICATION
# Peu de difficulté dans cet exercice, le seul point sur lequel il fallait porter attention était l'import du module math, qui permet d'obtenir une valeur précise de pi, sans avoir besoin d'entrer le nombre à la main.

# Le reste est assez simple, le symbole * permet de multiplier, tandis que le symbole ** permet de calculer le rayon puissance 3. Le symbole pour la division est la barre oblique (/). Pour obtenir le bon résultat, il fallait faire attention également aux parenthèses dans votre calcul.
