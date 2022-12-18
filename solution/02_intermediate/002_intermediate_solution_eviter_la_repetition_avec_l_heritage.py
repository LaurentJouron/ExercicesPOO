class Personnage:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom


class Magicien(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom=prenom, nom=nom)
        self.puissance = 80


class Gobelin(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom=prenom, nom=nom)
        self.puissance = 20


class Chevalier(Personnage):
    def __init__(self, prenom, nom):
        super().__init__(prenom=prenom, nom=nom)
        self.puissance = 70

"""
Éviter la répétition avec l'héritage - Solution

CODE:
    class Personnage:
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
 
    class Magicien(Personnage):
        def __init__(self, prenom, nom):
            super().__init__(prenom=prenom, nom=nom)
            self.puissance = 80

    class Gobelin(Personnage):
        def __init__(self, prenom, nom):
            super().__init__(prenom=prenom, nom=nom)
            self.puissance = 20
 
    class Chevalier(Personnage):
        def __init__(self, prenom, nom):
            super().__init__(prenom=prenom, nom=nom)
            self.puissance = 70

EXPLICATIONS:
    Cet exercice comportait beaucoup de tests à réussir mais il était
    finalement assez simple à réaliser si vous maîtrisez le concept d'héritage.
    Pour éviter la répétition des attributs prenom et nom dans les trois
    classes, il fallait créer une classe Personnage qui définissait ces deux
    attributs :
    class Personnage:
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
            
    Cela nous permet de créer un personnage de la sorte :

    perso = Personnage(prenom='Gandalf', nom='LeGris')
    Dans notre cas, on ne veut pas créer directement un personnage, mais
    utiliser cette classe comme classe 'parente' de nos trois classes Magicien,
    Gobelin et Chevalier. Il suffisait donc d'indiquer cette classe dans la
    définition de nos trois classes :
    class Personnage:
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
     
    class Magicien(Personnage):
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
            self.puissance = 80

    class Gobelin(Personnage):
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
            self.puissance = 20
 
    class Chevalier(Personnage):
        def __init__(self, prenom, nom):
            self.prenom = prenom
            self.nom = nom
            self.puissance = 70
    C'est mieux, mais on répète encore trois fois la déclaration des attributs
    prenom et nom dans chacune des classes.
    Pour remédier à cette répétition, il faut appeler la méthode __init__ de la
    classe dont on hérite.
    Pour cela, le plus simple est d'utiliser la fonction super et de passer
    les valeurs de nom et prenom à la méthode __init__ :
    class Magicien(Personnage):
        def __init__(self, prenom, nom):
            super().__init__(prenom=prenom, nom=nom)
            self.puissance = 80
    On peut ainsi créer un magicien comme ceci :
    gandalf = Magicien(prenom='Gandalf', nom='LeGris')
    
    La fonction super va appeler la méthode __init__ de la classe Personnage et
    passer en argument "Gandalf" et "LeGris" aux paramètres prenom et nom
    définit dans la méthode __init__ de la classe Personnage.
    On répète la même opération pour les autres classes et cela permet d'éviter
    la répétition.
    L'attribut puissance quant à lui est différent pour chaque instance, on
    peut donc le laisser dans chaque classe.
    On aurait pu également le définir dans la classe Personnage et passer la
    valeur désirée lors de l'appel de la méthode __init__ comme ceci :
    class Personnage:
        def __init__(self, prenom, nom, puissance):
            self.prenom = prenom
            self.nom = nom
            self.puissance = puissance
     
    class Magicien(Personnage):
        def __init__(self, prenom, nom):
            super().__init__(prenom=prenom, nom=nom, puissance=80)
     
    class Gobelin(Personnage):
        def __init__(self, prenom, nom):
            super().__init__(prenom=prenom, nom=nom, puissance=20)
     
    class Chevalier(Personnage):
        def __init__(self, prenom, nom):
            super().__init__(prenom=prenom, nom=nom, puissance=70)

POINTS IMPORTANTS À RETENIR:
    Pour hériter d'une classe, on indique le nom de la classe à l'intérieur des
    parenthèses lors de la définition de la classe.
    Pour appeler une méthode de la classe dont on hérite, on peut utiliser la
    fonction super.
"""
