class Voiture:
    def __init__(self):
        self.marque = "Mazda"
        self.couleur = "Rouge"

    def recuperer_couleur(self):
        return self.couleur


mazda_rouge = Voiture()
couleur = mazda_rouge.recuperer_couleur()

"""
Trouver les erreurs - Solution

CODE:
    class Voiture:
        def __init__(self):
            self.marque = "Mazda"
            self.couleur = "Rouge"
     
        def recuperer_couleur(self):
            return self.couleur

    mazda_rouge = Voiture()
    couleur = mazda_rouge.recuperer_couleur()

EXPLICATIONS:
    Beaucoup d'erreurs disséminées dans ce script ! Bravo si vous les avez 
    toutes trouvées.
    Premièrement, il fallait remplacer def Voiture par Class Voiture.
    L'instruction def sert à déclarer des fonctions. Pour créer une classe, *
    on utilise l'instruction class.

    class Voiture:
    À l'inverse, à la deuxième ligne, il fallait utiliser def au lieu de class
    pour définir la méthode __init__ : 
    Il manquait également un tiret du bas avant et après le nom de la méthode 
    init. En effet, il faut deux tirets du bas avant et après le nom de la 
    méthode init. On avait donc deux erreurs sur la même ligne! 
    def __init__(self):
    Ensuite, il fallait ajouter self devant le nom des attributs marque et
    couleur:
    self.marque = "Mazda"
    self.couleur = "Rouge"
    Sans le self ces deux noms n'étaient que des variables définies à 
    l'intérieur de la méthode __init__.
    Dans notre cas, on voulait créer des attributs d'instance, il fallait donc 
    ajouter le self.
    Il manquait également un self dans la méthode recuperer_couleur :
    def recuperer_couleur(self):
    Il ne faut jamais oublier de mettre self en premier paramètre pour pouvoir
    récupérer l'instance.
    La seule façon de faire qui permette d'omettre le self est d'utiliser le 
    décorateur @staticmethod pour rendre la méthode statique.
    À l'intérieur de la méthode recuperer_couleur, il fallait là encore ajouter
    un self pour retourner l'attribut couleur de la voiture :
    def recuperer_couleur():
        return self.couleur
    Pour finir, il manquait les parenthèses lors de la création de l'instance 
    mazda_rouge. 
    mazda_rouge = Voiture()
    Sans ces parenthèses, on fait juste associer le nom mazda_rouge à la classe
    Voiture.
    Cela n'a pas grand intérêt, à part d'utiliser ce nom pour créer une 
    instance, par exemple cela permettrait de faire :
    voiture = mazda_rouge()
    Mais nous ce que l'on veut dans ce cas-ci c'est bien créer une instance de
    Voiture que l'on retourne dans le nom mazda_rouge. Il fallait donc ajouter
    les parenthèses après Voiture.

POINTS IMPORTANTS À RETENIR:
    Pour créer une classe, on utilise l'instruction class.
    Pour définir une méthode, on utilise l'instruction def.
    Pour initialiser une instance, on utilise la méthode 'magique' __init__.
    Pour définir un attribut d'instance, on doit le préfixer du mot self.
    Pour définir une méthode, on doit obligatoirement mettre en premier
    paramètre self (à moins d'utiliser le décorateur @staticmethod pour créer
    une méthode statique).
    Pour créer une instance à partir d'une classe, on utilise le nom de la
    classe suivie de parenthèses.
"""