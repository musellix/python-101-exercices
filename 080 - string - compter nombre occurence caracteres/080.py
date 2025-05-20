# Alors dans cet exercice on va faire un vérificateur de codes Python.
# On va tout simplement dans cet exercice vérifier une seule chose, c'est si notre code contient bien
# le bon nombre de parenthèses.


# SOLUTION
code = "print(any(('py' or 'txt') in ext for ext in ['.py', '.obj', '.json]))"

nb_parentheses_ouvrantes = 0
nb_parentheses_fermantes = 0

for caractere in code:
    # print(caractere)
    if caractere == "(":
        nb_parentheses_ouvrantes += 1
    elif caractere == ")":
        nb_parentheses_fermantes += 1

print(nb_parentheses_ouvrantes == nb_parentheses_fermantes)

# ------------------

code = "print(any(('py' or 'txt') in ext for ext in ['.py', '.obj', '.json]))"
print(code.count('(') == code.count(')'))

# EXPLICATION

