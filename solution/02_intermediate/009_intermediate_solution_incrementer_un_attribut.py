class Etudiant:
    repertoire = []

    def __init__(self, nom, prenom):
        self.prenom = prenom
        self.nom = nom
        self.uid = len(Etudiant.repertoire) + 1
        Etudiant.repertoire.append(self)


john = Etudiant("John", "Smith")
julie = Etudiant("Julie", "Martin")
marc = Etudiant("Marc", "Tremblay")
print(Etudiant.repertoire)
print(marc.uid)

"""
Incrémenter un attribut - Solution

CODE:
    class Etudiant:
        repertoire = []
     
        def __init__(self, nom, prenom):
            self.prenom = prenom
            self.nom = nom
            self.uid = len(Etudiant.repertoire) + 1
            Etudiant.repertoire.append(self)

    john = Etudiant("John", "Smith")
    julie = Etudiant("Julie", "Martin")
    marc = Etudiant("Marc", "Tremblay")
    print(Etudiant.repertoire)
    print(marc.uid)

EXPLICATIONS:
    Cet exercice n'était pas très compliqué mais il fallait tout de même 
    réfléchir un peu pour trouver un moyen de générer automatiquement un 
    identifiant unique.
    Pour cela, on se sert de l'attribut repertoire de la classe Etudiant auquel
    on ajoute chaque instance créée.
    En utilisant la fonction len, on peut récupérer la longueur de la liste et 
    s'en servir pour générer l'identifiant unique :
    self.uid = len(Etudiant.repertoire) + 1
    On ajoute 1 à la longueur de la liste car on ajoute l'étudiant à la ligne 
    d'après.
    On pourrait également inverser les deux lignes (ajouter d'abord l'instance)
    et ainsi éviter d'avoir à ajouter 1. Cela revient au même.
    Une fois l'identifiant unique généré, on ajoute l'instance (donc self) dans
    la liste avec la méthode append, tout simplement :
    Etudiant.repertoire.append(self)

POINTS IMPORTANTS À RETENIR:
    Pour accéder à un attribut de classe, on utilise directement la classe
    (MaClasse.mon_attribut).
    Pour récupérer la longueur d'une liste, on utilise la fonction len.
"""