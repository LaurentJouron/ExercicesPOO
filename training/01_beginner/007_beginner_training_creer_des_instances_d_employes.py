"""
Créer des instances employés
    Dans cet exercice, vous disposez d'une classe Entreprise qui contient un
    attribut de classe employes :
    class Entreprise:
        employes = []
    Cet attribut est une liste qui doit contenir les employés de l'entreprise.
    Le but de cet exercice, est de créer des instances d'employés à partir de
    la liste de tuples employes :
    employes = [
                ("Pierre", "Smith", "Responsable RH", 35000),
                ("Julie", "Martin", "Développeur Python", 42000),
                ("Éric", "Dupont", "Chef de projet", 50000),
                ]
    Chaque instance d'employé créé à partir de la classe Employe doit être
    ajouté à l'attribut de classe employes de la classe Entreprise.
    L'attribut employes de la classe Entreprise, doit donc à la fin de
    l'exercice contenir trois instances de la classe Employe :
    # >>> print(Entreprise.employes)
    [<__main__.Employe object at 0x102356860>,
     <__main__.Employe object at 0x102356898>,
     <__main__.Employe object at 0x1023568d0>]

Astuces:
    Pour créer les instances d'employés, il faut boucler sur la liste employes
    avec une boucle for.
    L'attribut de classe employes de la classe Entreprise est une liste. Pour
    ajouter les instances créées à cet attribut, il suffit donc d'utiliser la
    méthode append.
"""


class Entreprise:
    employes = []


class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire


employes = [
            ("Pierre", "Smith", "Responsable RH", 35000),
            ("Julie", "Martin", "Développeur Python", 42000),
            ("Éric", "Dupont", "Chef de projet", 50000),
            ]


# Moi
# for employe in employes:
#     Entreprise.employes.append(employe)
# print(Entreprise.employes)


# Correction
for employe_data in employes:
    employe = Employe(*employe_data)
    Entreprise.employes.append(employe)
print(Entreprise.employes)
