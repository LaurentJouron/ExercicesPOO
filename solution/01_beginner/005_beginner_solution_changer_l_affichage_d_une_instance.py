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


"""
Changer l'affichage d'une instance - Solution

CODE:

    class Entreprise:
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

EXPLICATIONS:
    Pour réussir cet exercice, il fallait ajouter à la classe Employe la 
    méthode spéciale __repr__ qui permet de changer la représentation des 
    instances de la classe :

    def __repr__(self):
        return f"{self.prenom} {self.nom}"
        
    À l'intérieur de cette méthode, on retourne tout simplement le prénom et le
    nom de notre instance (respectivement self.prenom et self.nom) que l'on 
    formate à l'intérieur d'une chaîne de caractères grâce aux f-string.
    
POINTS IMPORTANTS À RETENIR:
    Pour changer la représentation d'une instance, on implémente la méthode 
    'spéciale' __repr__ dans laquelle on peut retourner une chaîne de 
    caractères qui sera affichée.
"""