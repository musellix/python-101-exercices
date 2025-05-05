
# 033 - Inverser les lettres d'un mot
# Notions abordées : les chaînes de caractères.

# Dans cet exercice, vous allez devoir inverser l'ordre des lettres d'un mot.

# Dans cet exemple, le mot est 'Udemy' votre script doit donc retourner la chaîne de caractère 'Ymedu'. 

# Pour valider l'exercice, il faut que la première lettre de votre chaîne de caractères résultat soit en majuscule ('Ymedu' et non 'ymedU').

# Aller plus loin : Faites tenir votre script en une seule ligne.



# SOLUTION
mot = "Udemy"
a = mot[::-1].capitalize()
print(a)

# ------

mot = "Udemy"
resultat = []
 
for lettre in reversed(mot):
    resultat.append(lettre)
 
resultat_formate = "".join(resultat)
print(resultat_formate.capitalize())


# EXPLICATION
# Pour inverser une chaîne de caractère, on peut utiliser le slicing [::-1] ou la fonction reversed.
# Pour joindre les éléments d'une liste ensemble, on utilise la fonction join.
# Pour mettre une majuscule sur la première lettre d'un mot, on utilise la fonction capitalize.
