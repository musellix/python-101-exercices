# Dans l'exercice précédent, on a vu comment générer un mot de passe aléatoire
# Donc dans cet exercice, le but, ça va être de vérifier si ce mot de passe est valide, basé sur trois conditions
# La première condition, ça va être de vérifier si le mot de passe contient au moins deux nombres
# La deuxieme condition, ça va être de vérifier s'il contient une majuscule
# La troisième condition, on va vérifier qu'il fasse bien au moins huit caractères


import string
import random

characters = string.ascii_letters + string.digits + string.punctuation
mdp = ""
    
isMdpOk = False
while not isMdpOk:
    taille = random.randint(4, 12)
    mdp = ''.join(random.choice(characters) for _ in range(taille))

    isMdpOk = True
    nbChiffre = 0
    for i in mdp:
        if i.isdigit():
            nbChiffre += 1
    if nbChiffre < 2:
        isMdpOk = False

    if not any(i.isupper() for i in mdp):
        isMdpOk = False

    if len(mdp) < 8:
        isMdpOk = False

print(mdp)

# ----------------------------

import string
import random
 
taille = random.randint(4, 12)
 
lettres = string.ascii_letters + string.digits + string.punctuation
mot_de_passe = ''.join(random.choice(lettres) for l in range(taille))
 
print(mot_de_passe)
 
def verificateur_mdp(mdp):
    if len(mdp) >= 8 and any(l.isupper() for l in mdp) and len([n for n in mdp if n.isdigit()]) >= 2:
	return True
    return False
 
succes = verificateur_mdp(mot_de_passe)
print(succes)
