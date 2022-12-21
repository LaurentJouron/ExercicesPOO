"""
Créer une classe employé:
    Dans cet exercice, vous devez créer une classe Employe qui permettra de
    créer des employés qui auront 4 attributs :
    prenom
    nom
    position
    salaire
    On doit donc pouvoir avec votre script créer une instance de la sorte :
    john = Employe("John", "Smith", "Développeur Python", 45000)

Astuces:
    N'oubliez pas de définir la méthode __init__ pour initialiser votre
    instance avec les 4 attributs demandés.
"""

class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire

john = Employe('John', 'Smith', 'Developpeur Python', 45000)
