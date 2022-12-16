class Livre:
    prix = 9.99

"""
Créer un attribut de classe - Solution

CODE:
    class Livre:
        prix = 9.99


EXPLICATIONS:    
    Pour créer un attribut de classe, c'est très simple, il suffit de déclarer 
    une variable directement à l'intérieur du bloc d'instruction appartenant 
    à la classe.
    Pas besoin de self ou quoi que ce soit d'autre vu que l'attribut appartient 
    directement à la classe.
    On peut par la suite accéder à l'attribut comme suit :
    >>> Livre.prix
    9.99

POINTS IMPORTANTS À RETENIR:
    Pour créer un attribut de classe, on le définit directement à l'intérieur 
    de la classe, sans avoir besoin d'utiliser self.
"""