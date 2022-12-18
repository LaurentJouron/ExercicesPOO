class Cube:
    def __init__(self, x=5, y=2, z=7):
        self.x = x
        self.y = y
        self.z = z

    def move_x(self):
        self.x += 1


mon_cube = Cube()
mon_cube.move_x()


"""
Ajouter les self - Solution

CODE:
    class Cube:
        def __init__(self, x=5, y=2, z=7):
            self.x = x
            self.y = y
            self.z = z

        def move_x(self):
            self.x += 1

    mon_cube = Cube()
    mon_cube.move_x()

EXPLICATIONS:
    La première chose à laquelle il faut penser quand on crée des méthodes,
    c'est de toujours ajouter self comme premier paramètre.
    Il fallait donc ajouter self à la méthode __init__ et à la méthode move_x :

    class Cube:
        def __init__(self, x=5, y=2, z=7):
            x = x
            y = y
            z = z

        def move_x(self):
            x += 1

    mon_cube = Cube()
    mon_cube.move_x()

    Enfin, il fallait associer les attributs x, y et z à l'instance mon_cube.

    Pour cela, il fallait préfixer chaque variable par self. self représente
    l'instance (donc mon_cube dans ce cas-ci).

    On peut ainsi accéder à self.x à l'intérieur de la méthode move_x et
    incrémenter sa valeur de 1 :

    class Cube:
        def __init__(self, x=5, y=2, z=7):
            self.x = x
            self.y = y
            self.z = z

        def move_x(self):
            self.x += 1

    mon_cube = Cube()
    mon_cube.move_x()

POINTS IMPORTANTS À RETENIR:
    self représente l'instance, dans ce cas-ci l'instance mon_cube, créée à
    partir de la classe Cube.
    Les méthodes d'une classe doivent posséder au moins un paramètre, self,
    pour récupérer l'instance.
"""
