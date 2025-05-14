# Dans cet exercice.
# Le but, ça va être de faire un script qui va vérifier à l'intérieur d'un dossier s'il trouve le dossier
# qu'on veut chercher avec un temps de rafraîchissement


# SOLUTION
import os 
import threading
import time

dossier_depart = "D:/projets/python-101-exercices/069 - surveiller un dossier"
dossier_a_trouver = "trouve"

clearInterval = False

def rechercher_dossier(dossier_depart, dossier_a_trouver):
    global clearInterval
    chemin_complet = os.path.join(dossier_depart, dossier_a_trouver)
    if os.path.isdir(chemin_complet):
        print("Trouvé !!")
        clearInterval = True
    else:
        print("Dossier introuvable...")


def setInterval():
    global clearInterval
    while not clearInterval:
        print(clearInterval)
        rechercher_dossier(dossier_depart, dossier_a_trouver)
        time.sleep(3)


# Créer un thread pour exécuter la méthode à intervalles réguliers
thread = threading.Thread(target=setInterval)
thread.start()

# -------------------------

import os
import time
 
dossier = "/Users/thibh/Desktop"
dossier_a_chercher = "Python"
 
while dossier_a_chercher not in os.listdir(dossier):
	print("Dossier introuvable...")
	time.sleep(3)
 
print("Trouvé!")



# EXPLICATION