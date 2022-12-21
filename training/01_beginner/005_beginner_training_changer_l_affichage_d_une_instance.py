"""
Changer l'affichage d'une instance
    Dans cet exercice, vous devez ajouter une méthode 'spéciale' à la classe
    Employe pour changer l'affichage des instances de cette classe.
    En effet, avec le code de départ, si on affiche les instances contenues
    dans l'attribut Entreprise.employes, on obtient le résultat suivant, qui
    n'est pas très explicite :
    [<__main__.Employe object at 0x102356860>,
     <__main__.Employe object at 0x102356898>,
     <__main__.Employe object at 0x1023568d0>]
    À la place, on aimerait afficher le prénom et le nom des employés, comme
    ceci:
    [Pierre Smith,
     Julie Martin,
     Éric Dupont]
    Vous devez donc utiliser cette méthode 'magique' pour changer la
    représentation des instances.

Astuces:
    Pour changer la représentation d'une instance, il faut implémenter la
    méthode __repr__.
"""


class Entreprise:
    nom = "Docstring"
    employes = []


class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire

    def __repr__(self):
        return f"{self.prenom} {self.nom}"

employes = [
            ("Pierre", "Smith", "Responsable RH", 35000),
            ("Julie", "Martin", "Développeur Python", 42000),
            ("Éric", "Dupont", "Chef de projet", 50000),
            ]

for employe_data in employes:
    employe = Employe(*employe_data)
    Entreprise.employes.append(employe)
