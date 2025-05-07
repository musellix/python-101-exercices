# Le but de cet exercice, c'est d'afficher une phrase tant qu'un utilisateur le demande.
# on a un compteur qui se lance qui démarre à zéro.

# On nous demande si on veut continuer, donc on nous laisse le choix, oui ou non de continuer.
# Et tant que je vais dire oui,le compteur va s'incrémenter et on va continuer à exécuter le
# script.

# Lorsque je mets n pour non, on va sortir du script, arrêter le script et arrêter le compteur.


# SOLUTION

compteur = 0

while True:
    print(f"Le compteur est maintenant à {compteur}")

    continuer = input("Voulez vous continuer ? o/n : ")

    if continuer == "n":
        break
    elif continuer == "o":
        compteur += 1

