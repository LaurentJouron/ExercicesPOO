class Eleve:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def __repr__(self):
        return f"{self.prenom} {self.nom}"


class Classe:
    eleves = []

    @staticmethod
    def ajouter_eleve(prenom, nom):
        eleve = Eleve(prenom=prenom, nom=nom)
        Classe.eleves.append(eleve)


Classe.ajouter_eleve("John", "Smith")
print(Classe.eleves)


"""
Gérer une classe d'élèves - Solution

CODE:
    class Eleve:
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
     
        def __repr__(self):
            return "{} {}".format(self.prenom, self.nom)
     
    class Classe:
        eleves = []
     
        @staticmethod
        def ajouter_eleve(prenom, nom):
            eleve = Eleve(prenom=prenom, nom=nom)
            Classe.eleves.append(eleve)
     
    Classe.ajouter_eleve("John", "Smith")
    print(Classe.eleves)

EXPLICATIONS:

    Pour commencer, nous allons modifier la représentation des instances de la
    classe élève, grâce à la méthode __repr__ et la méthode format :
    def __repr__(self):
        return "{} {}".format(self.prenom, self.nom)
    Ainsi, quand on affiche une instance d'élève, on affichera son prénom et 
    son nom au lieu de l'adresse en mémoire de l'instance.
    Nous devions ensuite créer une méthode statique ajouter_eleve qui permette
    d'ajouter un élève avec un prénom et un nom.
    Pour ça on utilise le décorateur @staticmethod pour que la méthode soit
    statique.
    On donne deux paramètres à la méthode, prenom et nom :
    @staticmethod
    def ajouter_eleve(prenom, nom):
    Pour finir, il suffisait de créer une instance d'élève à partir des valeurs
    passées aux paramètres prenom et nom de la méthode ajouter_eleve. 
    On crée également un attribut de classe eleves (une liste vide) pour 
    stocker les instances d'élèves créées :
    class Classe:
        eleves = []
     
        @staticmethod
        def ajouter_eleve(prenom, nom):
            eleve = Eleve(prenom=prenom, nom=nom)
            Classe.eleves.append(eleve)

POINTS IMPORTANTS À RETENIR:
    Pour créer une méthode statique, on utilise le décorateur @staticmethod.
    Pour créer un attribut de classe, on le définit directement en dessous de
    la définition de la classe.
    Pour modifier la représentation d'une instance, on utilise la méthode 
    __repr__.
"""