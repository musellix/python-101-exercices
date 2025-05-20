
# 081 - Compter le nombre de phrases dans un texte
# Notions abordées : les chaînes de caractères.

# Dans cet exercice, le but est de compter le nombre de phrase présente dans le texte contenu dans la variable lorem. 
# Ce texte contient 4 phrases, votre script devra donc retourner le nombre 4.


# SOLUTION
lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
		   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
		   Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
		   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

loremList = [phrase for phrase in lorem.split(".") if phrase.strip()]
print(len(loremList))

# ----------------------------

print(lorem.count("."))



# EXPLICATION
# Pour compter le nombre de fois qu'un caractère apparaît dans une chaîne de caractère, on utilise la méthode 'count'.
