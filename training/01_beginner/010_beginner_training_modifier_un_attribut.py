"""
Modifier un attribut
    Dans cet exercice, vous devez créer une méthode changer_prix qui permette
    de modifier le prix de l'instance harry_potter :
    harry_potter.changer_prix(prix=14.99)
    Le prix de l'instance harry_potter doit être de 14.99 à la fin du script.
    Le prix la classe Livre doit lui rester à 9.99.
"""


class Livre:
    prix = 9.99

    def __init__(self, prix):
        self.prix = prix


harry_potter = Livre(19.99)
harry_potter.changer_prix(prix=14.99)
