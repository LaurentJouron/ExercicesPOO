class Cube:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


cube = Cube()
cube.set_position(1, 2, 3)


"""
Trouver les erreurs - Solution

CODE:
    class Cube:
        def __init__(self, x=0, y=0, z=0):
            self.x = x
            self.y = y
            self.z = z
     
        def set_position(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
     
    cube = Cube()
    cube.set_position(1, 2, 3)

EXPLICATIONS:    
    Le premier élément qu'il fallait corriger était la définition de la méthode
    set_position.
    
    Dans le script de départ, cette méthode ne contenait pas le paramètre self 
    en première position, ce qui n'est pas possible pour une fonction définie 
    à l'intérieur d'une classe (à moins d'utiliser le décorateur staticmethod):
    
    def set_position(self, x, y, z):
    Ensuite, il fallait assigner les valeurs de x, y et z à l'instance, et donc
     à self à l'intérieur de la méthode :
    
    {‌{ "
    def set_position(self, x, y, z):
        self.x = x
        self.y = y

POINTS IMPORTANTS À RETENIR:
    Une fonction contenue à l'intérieur d'une classe doit obligatoirement 
    contenir un paramètre pour récupérer l'instance. Par convention, on utilise
    le nom self pour ce premier paramètre.

    Pour récupérer ou modifier l'attribut d'une instance, il faut donc accéder
    à cet attribut via le paramètre self. Donc pour assigner une valeur à 
    l'attribut x de l'instance à l'intérieur d'une méthode, il faut faire 
    self.x = valeur.
"""