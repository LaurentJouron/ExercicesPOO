"""
Empêcher la modification d'un attribut
    Le but de cet exercice est d'empêcher la modification de l'attribut numero
    de l'instance john.
    Je ne vous en dis pas plus, à vous de trouver un moyen d'empêcher le
    numéro d'être modifié.
    Si on essaie de modifier l'attribut, le script doit retourner une erreur de
    type AttributeError.

Astuces:
    Pour empêcher la modification d'un attribut, vous pouvez passer par les
    propriétés et lever une exception quand on essaie de modifier la valeur de
    l'attribut numero.
"""

class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance

john = Compte(nom="John Smith", numero="123456", balance=20000)