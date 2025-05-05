
# 032 - Formater une chaîne de caractères
# Notions abordées : les chaînes de caractères.

# Le but de cet exercice est d'afficher dans le print le nom et le prenom contenu dans les variables respectives.
# prenom = "Pierre"
# nom = "Dupont"
# print("Bonjour je m'appelle")

# Votre script doit donc afficher : 'Bonjour je m'appelle Pierre Dupont'.


# SOLUTION
prenom = "Pierre"
nom = "Dupont"
 
print(f"Bonjour je m'appelle {prenom} {nom}")
 
# Solution alternative avec la méthode format
print("Bonjour je m'appelle {prenom} {nom}".format(prenom=prenom, nom=nom))


# EXPLICATION
# Pour concaténer des chaînes de caractères, on peut utiliser une f-string, pour insérer directement à l'intérieur de la chaîne des variables grâce aux accolades.
