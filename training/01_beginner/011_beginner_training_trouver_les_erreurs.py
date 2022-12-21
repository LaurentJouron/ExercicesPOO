"""
Trouver les erreurs
    Dans cet exercice, vous devez corriger le script pour que la méthode
    set_position fonctionne correctement et modifie les attributs x, y et z de
    l'instance cube.
    Votre script doit donc redéfinir les valeurs de ces trois attributs qui
    devront être égaux à 1 pour x, 2 pour y et 3 pour z.
    Une fonction à l'intérieur d'une classe doit posséder un premier paramètre
    qui permette de récupérer l'instance (ce paramètre est, par convention,
    appelé self).
"""


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
print(cube.x, cube.y, cube.z)