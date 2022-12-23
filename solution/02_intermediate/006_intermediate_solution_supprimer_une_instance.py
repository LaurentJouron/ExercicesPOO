etudiants_partis = []

class Etudiant:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def __del__(self):
        etudiants_partis.append(f"{self.prenom} {self.nom}")

john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")

del marc

"""
Supprimer une instance - Solution

CODE:
    etudiants_partis = []     
     
    class Etudiant:
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
        def __del__(self):
            etudiants_partis.append('{} {}'.format(self.prenom, self.nom))
    john = Etudiant('John', 'Smith')
    julie = Etudiant('Julie', 'Martin')
    marc = Etudiant('Marc', 'Tremblay')
    del marc

EXPLICATIONS:
    Pour exécuter du code lors de la suppression d'une instance avec 
    l'instruction del, il faut utiliser la méthode __del__.
    À l'intérieur de cette méthode, nous ajoutons tout simplement le prénom et
    le nom de l'étudiant qui a été supprimé, avec les f-string :
    
    def __del__(self):
        etudiants_partis.append(f'{self.prenom} {self.nom}')
    À chaque fois qu'on supprime une instance de la classe Etudiant, on ajoute
    ainsi le prénom et le nom de l'étudiant supprimé à la liste 
    etudiants_partis.

POINTS IMPORTANTS À RETENIR:
    Pour exécuter une action quand on supprime une instance, il faut 
    implémenter la méthode __del__.
"""