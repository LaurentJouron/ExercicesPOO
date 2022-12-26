"""
Générer un attribut aléatoire
    Dans cet exercice, vous devez implémenter une méthode virement qui permette
    d'ajouter ou enlever de l'argent à la balance du compte.
    On désire générer un numéro unique pour chaque virement effectué et le
    sauvegarder dans le dictionnaire virements de l'instance.
    Le numéro unique généré doit contenir 15 caractères et peut être composé de
    lettres (minuscules ou majuscules) et de chiffres de 0 à 9.
    Dans le cas de cet exercice, john effectue un virement de 5,000€.
    Le dictionnaire john.virements devra donc ressembler à:
    >>> john.virements
    {'vQLONfX81hrIsDS': 5000}
    Bien sûr, la clé du virement étant aléatoire, votre script retournera un
    résultat différent pour le numéro unique du virement.
    La balance du compte de John devra être égale à 25,000€ (20,000€ de départ
    plus les 5,000€ du virement).

Astuces:
    Pour générer des caractères aléatoires, vous pouvez utiliser le module
    random et le module string.
"""


class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance
        self.virements = {}


john = Compte(nom="John Smith", numero="123456", balance=20000)
john.virement(montant=5000)