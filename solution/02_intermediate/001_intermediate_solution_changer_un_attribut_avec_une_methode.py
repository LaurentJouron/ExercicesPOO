class Voiture:
    def __init__(self, marque, prix):
        self.marque = marque
        self.prix = prix

    def changer_prix(self, prix):
        if isinstance(prix, int):
            self.prix = prix


voiture = Voiture(marque="Mazda", prix=30000)
voiture.changer_prix(35000)

"""
Changer un attribut avec une méthode - Solution

CODE:
    class Voiture:
        def __init__(self, marque, prix):
            self.marque = marque
            self.prix = prix
     
        def changer_prix(self, prix):
            if isinstance(prix, int):
                self.prix = prix
    voiture = Voiture(marque="Mazda", prix=30000)
    voiture.changer_prix(35000)

EXPLICATIONS:
    La première chose à faire était de créer la méthode __init__ afin de
    pouvoir initialiser les attributs marque et prix sur l'instance :

    class Voiture:
        def __init__(self, marque, prix):
            self.marque = marque
            self.prix = prix
    Vous deviez ensuite créer une méthode changer_prix qui permette de modifier
     le prix :
    class Voiture:
        def __init__(self, marque, prix):
            self.marque = marque
            self.prix = prix
     
        def changer_prix(self, prix):
            self.prix = prix
Jusque-là rien de bien compliqué.

La dernière chose à faire était de modifier l'attribut prix, seulement si
celui-ci était un nombre entier.
Pour cela, on utilise la fonction isinstance qui permet de vérifier si une
variable est d'un certain type (on pourrait également utiliser la fonction
type, mais isinstance a l'avantage de gérer l'héritage. Je préfère donc
l'utiliser plutôt que la fonction type):
    class Voiture:
        def __init__(self, marque, prix):
            self.marque = marque
            self.prix = prix
     
        def changer_prix(self, prix):
            if isinstance(prix, int):
                self.prix = prix

Avec if isinstance(prix, int): on vérifie que la valeur passée en argument au
paramètre prix est bien de type int (nombre entier).
Si c'est le cas, on met à jour l'attribut prix de l'instance :
    self.prix = prix

POINTS IMPORTANTS À RETENIR:
    Pour vérifier si une variable est d'un certain type, on peut utiliser la
    fonction isinstance.
    Pour modifier un attribut d'instance, on fait une assignation comme si on
    modifiait une variable : self.mon_attribut = valeur.
"""