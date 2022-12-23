"""
Incrémenter un attribut
    Dans cet exercice, vous devez assigner un identifiant unique à chaque
    instance d'étudiant créée et ajouter les instances dans l'attribut de
    classe repertoire.
    Chaque instance créée à partir de la classe Etudiant doit posséder un
    attribut uid correspondant à son numéro d'étudiant.
    john devra donc avoir comme identifiant unique 1, julie devra avoir
    l'identifiant 2 et marc l'identifiant 3.
    Cet attribut doit être généré automatiquement. Si on crée un autre
    étudiant, celui-ci doit avoir un identifiant unique égal à 4.
    L'attribut repertoire de la classe Etudiant doit contenir toutes les
    instances d'étudiants créées.
"""

class Etudiant:
    repertoire = []

    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom


john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")
print(Etudiant.repertoire)
print(marc.uid)