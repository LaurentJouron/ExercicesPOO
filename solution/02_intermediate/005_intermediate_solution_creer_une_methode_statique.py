class Chanson:
    paroles = """Joyeux anniversaire,
Joyeux anniversaire,
Joyeux anniversaire {prenom},
Joyeux anniversaire."""

    @staticmethod
    def chante_pour(prenom):
        return Chanson.paroles.format(prenom=prenom)


print(Chanson.chante_pour(prenom="Paul"))

"""
Créer une méthode statique - Solution

CODE:    
    class Chanson:
        paroles = '''Joyeux anniversaire,
    Joyeux anniversaire,
    Joyeux anniversaire {prenom},
    Joyeux anniversaire.'''
     
        @staticmethod
        def chante_pour(prenom):
            return Chanson.paroles.format(prenom=prenom)
     
    print(Chanson.chante_pour(prenom="Paul"))

EXPLICATIONS:
    Pour rendre une méthode statique et ainsi pouvoir l'utiliser directement 
    depuis la classe, sans avoir besoin de créer d'instance, il faut utiliser 
    le décorateur @staticmethod :
    
    @staticmethod
    def chante_pour():
    Cela nous permet d'appeler directement la méthode chante_pour depuis la
    classe Chanson :
    Chanson.chante_pour()
    Il suffisait ensuite de permettre l'envoi d'un argument prenom et 
    d'afficher les paroles de la chanson contenues dans l'attribut paroles de 
    la classe Chanson :
    @staticmethod
    def chante_pour(prenom):
        return Chanson.paroles.format(prenom=prenom)
    Dans ce cas-ci, vu qu'on a une méthode statique, pas besoin de mettre le 
    paramètre self, vu qu'on n'a pas besoin d'instance.
    C'est l'avantage des méthodes statiques, de pouvoir travailler directement 
    à partir de la classe. Il suffisait donc d'ajouter un paramètre prenom.
    On retournait ensuite la chanson adaptée pour le prénom passé en argument 
    grâce à la méthode format:
    Chanson.paroles.format(prenom=prenom)

POINTS IMPORTANTS À RETENIR:
    Pour définir une méthode statique, on utilise le décorateur @staticmethod.
    Pour insérer la valeur d'une variable à l'intérieur d'une chaîne de
    caractères on peut utiliser la méthode format.
"""
