# 077 - Inverser l'ordre des mots dans une phrase
# Notions abordées : les chaînes de caractères, les boucles.

# On reprend un exercice que nous avons effectué plus tôt dans la formation mais cette fois-ci avec une phrase.

# Il est question ici d'inverser l'ordre des mots dans la phrase. Votre phrase devra, comme une phrase normalement construite, commencer par une majuscule.

# Nous avons ici la phrase 'Bonjour tout le monde', votre script devra donc retourner la phrase 'Monde le tout bonjour'.


# SOLUTION
phrase = "Bonjour tout le monde"
phrase = phrase.lower()
phrase = phrase.split()
phrase.reverse()

phrase = ' '.join(mot for mot in phrase)
phrase = phrase.capitalize()

print(phrase)

# --------------------

phrase = "Bonjour tout le monde"
phrase_split = phrase.split()
 
resultat = []
 
for mot in reversed(phrase_split):
    resultat.append(mot)
 
resultat_formate = " ".join(resultat).capitalize()
print(resultat_formate)


# EXPLICATION
# Pour inverser une liste, on peut utiliser la fonction reversed ou la syntaxe [::-1]
