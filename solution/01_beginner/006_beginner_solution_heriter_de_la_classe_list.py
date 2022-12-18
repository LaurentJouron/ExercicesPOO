class ListeCustom(list):
    pass


liste = ListeCustom()
liste.append(5)

"""
Hériter de la classe list - Solution

CODE:

    class ListeCustom(list):
        pass
    
    liste = ListeCustom()
    liste.append(5)

EXPLICATIONS:

    Pour créer une notion d'héritage entre une classe et une autre (avec une 
    relation 'parent' / 'enfant'), il faut indiquer la classe dont on veut 
    hériter dans les parenthèses lors de la définition de la classe :

    class ListeCustom(list):
        On peut hériter des classes de base de Python comme str, list etc.

    En héritant d'une classe, on accède automatiquement à toutes ses méthodes.
    Cela nous permet donc d'utiliser la méthode append sur l'instance créée
    à partir de notre classe ListeCustom:

    liste.append(5)

POINTS IMPORTANTS À RETENIR:
    Pour hériter d'une classe, il faut indiquer cette classe dans les 
    parenthèses lors de la définition de la classe.
"""