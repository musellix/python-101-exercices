# 029 - Récupérer la valeur d'une variable d'environnement
# Notions abordées : le module os

# Le but de cette exercice est de recuperer la valeur d'une variable d'environnement
# PYHTON_PATH ou encore HOME


# SOLUTION
import os

home_var = os.environ.get("HOME")
print(home_var)

python_var = os.environ.get("PYTHONPATH")
print(python_var)

