# Le but de cet exercice est de calculer le temps d'execution d'un script Python



# SOLUTION
from time import time

debut = time()
_ = [i*2 for i in range(9999999)]
fin = time()

print(f"Temps d'exécution : {fin - debut}s")
# Temps d'exécution : 0.9820413589477539s

