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
