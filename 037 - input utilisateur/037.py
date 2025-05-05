# Faire un script qui calcule l'age d'un chien en années humaines.

# chien agé de 0 à 2 ans : 
# age * 10.5

# chien agé de 2 ans et plus :
# (age - 2) * 4 + 21



age_chien = input("Quel âge a votre chien ? ")

if age_chien.isdigit():
    age_chien = int(age_chien)

    if age_chien < 0:
        print("L'âge d'un chien ne peut pas être négatif.") 
        exit()

    elif age_chien <= 2:
        age_humain = age_chien * 10.5
        print(f"L'âge de votre chien en années humaines est : {age_humain} ans.")

    else:
        age_humain = (age_chien - 2) * 4 + 21
        print(f"L'âge de votre chien en années humaines est : {age_humain} ans.")
