"""
Calculer l'aire d'un rectangle avec un ContextManager
    Dans cet exercice, vous allez devoir implémenter ce qu'on appelle un
    contextmanager.
    On doit en effet pouvoir utiliser notre classe Rectangle avec l'instruction
    with afin de permettre le calcul de l'aire d'un rectangle:
    with Rectangle(6, 12) as r:
        r.calcul_aire()
    Le code suivant devra retourner les deux phrases suivantes :
    L'aire d'un rectangle de 6m par 12m est de :
    72m2
    Vous devez donc implémenter le contextmanager ainsi que la méthode
    calcul_aire qui permette de calculer l'aire du rectangle (petit rappel:
    pour calculer l'aire d'un rectangle, il suffit de multiplier sa largeur
    par sa longueur).

Astuces:
    Pour implémenter un contextmanager, il faut implémenter les méthodes
    __enter__ et __exit__.
"""

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur


with Rectangle(6, 12) as r:
    r.calcul_aire()
