"""
Créer un héritage entre deux classes
    Dans cet exercice, vous devez faire hériter la classe Cube de la classe
    Shape.
    Vous devez en plus vous assurer que la classe Cube hérite des attributs
    d'instance définis dans la classe Shape (les attributs x et y de la méthode
    __init__).
    Comme un cube est en trois dimensions, vous devez en plus ajouter un
    attribut z qui n'existera que sur les instances de la classe Cube et non
    pas sur la classe Shape.
    Les trois attributs x, y et z doivent être définis à 0.
    Votre script devra donc afficher :
    0
    0
    0
    
Astuces:
    Pour appeler la méthode __init__ de la classe parent, on peut utiliser la
    fonction super.
"""


class Shape:
    def __init__(self):
        self.x = 0
        self.y = 0


class Cube(Shape):
    def __init__(self, z=0):
        super().__init__()
        self.z = z

cube = Cube()
print(cube.x)
print(cube.y)
print(cube.z)
