# 039 - Sortir d'une boucle infinie
# Notions abordées : boucle while.

# Dans cet exercice, nous sommes en présence d'une boucle while infinie ! En l'état actuel, le script ne s'arrêtera jamais et la phrase 'Exercice réussi !' ne s'affichera jamais.

# Vous devez modifier la boucle while afin d'en sortir et d'afficher la phrase 'Exercice réussi !'.

# i = 0

# while i < 10:
# 	pass
	
# print("Exercice réussi !")


# SOLUTION
i = 0
 
while i < 10:
    i += 1
 
print("Exercice réussi !")


# EXPLICATION
# Pour incrémenter un nombre entier, on utilise la syntaxe variable += 1
