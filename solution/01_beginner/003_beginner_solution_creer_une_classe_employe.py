class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire


"""
Créer une classe employé - Solution
CODE:
    class Employe:
    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire

EXPLICATIONS:
    Pour créer une classe, on utilise l'instruction class.
    Afin de pouvoir initialiser directement les instances créées avec des 
    attributs, on utilise la méthode __init__ qui contient 4 paramètres 
    (en plus du self):
    
    prenom
    nom
    position
    salaire

    Afin de créer des attributs sur notre instance, il faut assigner les 
    valeurs passées lors de la création de l'instance, à notre instance à 
    l'intérieur de la méthode __init__ (qui est récupérée par le paramètre 
    self):

    def __init__(self, prenom, nom, position, salaire):
        self.prenom = prenom
        self.nom = nom
        self.position = position
        self.salaire = salaire
    
    ⚠️ Notez que dans ce cas-ci, le nom des paramètres de la méthode__init__ 
    et le nom des attributs est le même, mais ce n'est pas une obligation ! 
    On pourrait très bien faire comme ceci :
    
    class Employe:
        def __init__(self, a, b, c, d):
            self.prenom = a
            self.nom = b
            self.position = c
            self.salaire = d
 
    John = Employe("John", "Smith", "Dev Python", 45000)
    
    Mais ça serait beaucoup moins clair, il vaut donc mieux utiliser des noms
    de paramètres explicites.

POINTS IMPORTANTS À RETENIR:

    Pour initialiser une instance, on utilise la méthode __init__.
    
    Pour créer un attribut d'instance à l'intérieur de la méthode __init__, 
    on utilise la syntaxe self.attribut = valeur.
"""