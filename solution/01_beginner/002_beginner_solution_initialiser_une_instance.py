class Livre:
    prix = 9.99

    def __init__(self, prix):
        self.prix = prix


harry_potter = Livre(19.99)

"""
Initialiser une instance - Solution

CODE:

    class Livre:
        prix = 9.99
     
        def __init__(self, prix):
            self.prix = prix
     
    harry_potter = Livre(19.99)

EXPLICATIONS:

    Pour initialiser une instance, on utilise la méthode __init__ qui est 
    appelée automatiquement lorsque l'on crée une instance.
    
    👉 À l'intérieur de cette méthode, il ne faut pas oublier de mettre en 
    premier paramètre self, qui correspond à notre instance, et va nous 
    permettre à l'intérieur de cette méthode de créer un attribut propre à 
    notre instance.
    
    Cet attribut prix est le deuxième paramètre que nous donnons à la méthode 
    __init__.
    
    Ainsi, nous pouvons définir un prix personnalisé pour notre instance au 
    moment de sa création :
    
    harry_potter = Livre(19.99)
    Et le récupérer pour l'assigner à notre instance (self) dans la méthode 
    __init__ :
    
    def __init__(self, prix):
        self.prix = prix
    Ainsi, on définit un attribut prix uniquement sur notre instance (self) 
    et l'attribut de classe prix reste inchangé à 9.99€.



POINTS IMPORTANTS À RETENIR:

    Pour initialiser une instance, on utilise la méthode __init__.
    
    Pour référer à notre instance à l'intérieur d'une méthode, on utilise le 
    paramètre self.
    
    Pour créer un attribut d'instance, on utilise la syntaxe 
    self.attribut = valeur.
"""