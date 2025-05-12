# Alors le but de cet exercice?
# Ça va être de séparer la liste de prénoms qu'on a devant nous en deux par rapport au milieu de l'alphabet.
# Donc, c'est quelque chose qu'on voit par exemple assez souvent dans les élections.


# SOLUTION
employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoe", "Nathan"]

employes_A_a_M = []
employes_N_a_Z = []

employes.sort()

for prenom in employes:
    if prenom[0] < "N":
        employes_A_a_M.append(prenom)
    else:
        employes_N_a_Z.append(prenom)

print(employes_A_a_M)
print(employes_N_a_Z)

# --------------------------

import string
 
employes = ["Pierre", "Marie", "Julien", "Astrid", "Zoé"]
 
alphabet = string.ascii_lowercase
milieu = int(len(alphabet) / 2)
alphabet_01, alphabet_02 = alphabet[:milieu], alphabet[milieu:]
 
employes_a_m = []
employes_n_z = []
 
for employe in employes:
    premiere_lettre = employe[0].lower()
    if premiere_lettre in alphabet_01:
        employes_a_m.append(employe)
    elif premiere_lettre in alphabet_02:
        employes_n_z.append(employe)
 
print("Employés de A à M:", ", ".join(sorted(employes_a_m)))
print("Employés de N à Z:", ", ".join(sorted(employes_n_z)))


# EXPLICATION
