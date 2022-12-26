class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def __enter__(self):
        print(f"L'aire d'un rectangle de {self.longueur}m par {self.largeur}m "
              f"est de :")
        return self
        
    def __exit__(self, exception_type, exception_value, callback):
        print(f"{self.aire} m2")
    
    def calcul_aire(self):
        self.aire = self.longueur * self.largeur


with Rectangle(6, 12) as r:
    r.calcul_aire()


"""'
Calculer l'aire d'un rectangle avec un ContextManager - Solution

CODE:
    class Rectangle:
        def __init__(self, longueur, largeur):
            self.longueur = longueur
            self.largeur = largeur
            
    def __enter__(self):
        print(f"L'aire d'un rectangle de {self.longueur}m par {self.largeur}m "
              f"est de :")
        return self
        
    def __exit__(self, exception_type, exception_value, callback):
        print(f"{self.aire} m2")
    
    def calcul_aire(self):
        self.aire = self.longueur * self.largeur
     
    with Rectangle(6, 12) as r:
        r.calcul_aire()

EXPLICATIONS:
    La première chose à faire était d'implémenter la méthode calcul_aire :

    def calcul_aire(self):
        self.aire = self.longueur * self.largeur
    Cette méthode est très simple et retourne l'aire du rectangle dans un 
    attribut aire.
    Maintenant, pour pouvoir utiliser l'instruction with, il fallait 
    implémenter un contextmanager.
    Pour ce faire, on utilise les deux méthodes spéciales __enter__ et __exit__.
    La méthode __enter__ est appelée au début du contexte et la méthode 
    __exit__ à sa sortie.
    Pour la méthode __enter__, on voulait juste annoncer le fait qu'on 
    s'apprête à calculer l'aire du rectangle. Un simple print suffisait donc:
    def __enter__(self):
        print("L'aire d'un rectangle de {}m par {}m est de :".format(self.longueur, self.largeur))
        return self
    Il ne faut cependant pas oublier de retourner self puisque c'est la valeur
    que l'on retourne dans la méthode __enter__ qui sera récupérée dans notre
    cas par la variable r lors de l'instruction with:
    with Rectangle(6, 12) as r:
        r.calcul_aire()
    À l'intérieur du bloc d'instruction, on appelle la méthode calcul_aire 
    afin de récupérer le résultat du calcul dans l'attribut aire.
    On peut ensuite afficher ce résultat à la sortie du contextmanager, dans
    la méthode __exit__:
    def __exit__(self, exception_type, exception_value, callback):
        print("{}m2".format(self.aire))
    La méthode __exit__ doit obligatoirement posséder trois paramètres pour 
    recueillir les informations pertinentes en cas d'erreur.
    👉 Le nom des paramètres n'a pas d'importance, ce qui compte c'est bien 
    d'en avoir trois, mais vous pourriez les appeler autrement et ça 
    fonctionnerait également.

POINTS IMPORTANTS À RETENIR:
    Pour implémenter un contextmanager, on utilise les méthodes __enter__ et 
    __exit__.
    Le contextemanager d'une classe est appelé automatiquement quand on 
    utilise l'instruction with.
"""