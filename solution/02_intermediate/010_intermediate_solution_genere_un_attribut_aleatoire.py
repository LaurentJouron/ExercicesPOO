import random
import string

class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance
        self.virements = {}

    def virement(self, montant):
        self.balance += montant
        uuid = "".join(random.sample(string.digits + string.ascii_letters, 15))
        self.virements[uuid] = montant


john = Compte(nom="John Smith", numero="123456", balance=20000)
john.virement(montant=5000)

"""
Générer un attribut aléatoire - Solution

CODE:
    import random
    import string

    class Compte:
        def __init__(self, nom, numero, balance):
            self.nom = nom
            self.numero = numero
            self.balance = balance
            self.virements = {}

        def virement(self, montant):
            self.balance += montant
            uuid = "".join(random.sample(string.digits + string.ascii_letters, 15))
            self.virements[uuid] = montant

    john = Compte(nom="John Smith", numero="123456", balance=20000)
    john.virement(montant=5000)

EXPLICATIONS:
    Premièrement, on devait créer une méthode virement qui permette de virer un
    certain montant d'argent dans le compte.
    On devait donc pouvoir récupérer ce montant dans un paramètre que l'on 
    appelle tout bonnement montant. On utilise la valeur envoyée à ce paramètre
    pour modifier la balance du compte :

    def virement(self, montant):
        self.balance += montant
    On devait ensuite générer un identifiant unique aléatoire composé de 15 
    lettres et chiffres.
    Pour cela, on fait appelle à deux modules : le module random et le module
    string.
    Le module string contient plusieurs constantes bien pratiques pour ce genre
    de cas.
    Dans le cadre de cet exercice, on utilise la constante string.ascii_letters
    qui contient toutes les lettres de l'alphabet en majuscule et minuscule:
    >>> import string
    >>> string.ascii_letters
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    De la même façon, la constante string.digits nous retourne tous les chiffres de 0 à 9 :

    >>> import string
    >>> string.digits
    '0123456789'
    Chacune de ces constantes nous retourne une chaîne de caractères qui 
    contient tous les caractères demandés.

    On peut donc additionner ces deux chaînes de caractères avec le symbole
    d'addition:
    >>> string.digits + string.ascii_letters
    '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    On a donc ainsi tous les caractères dans lesquels nous souhaitons 'piocher'
    pour générer notre identifiant aléatoire.

    Pour sélectionner un nombre aléatoire de caractères dans une chaîne de 
    caractères, on utilise la fonction sample du module random:
    >>> random.sample('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 15)
    ['v', 'r', 'm', 'P', 'o', 'g', 'x', 's', 'D', 'O', '3', 'q', 'y', 'b', 'V']

    Cette fois-ci, on se retrouve avec une liste. Il nous faut donc joindre les
    éléments de cette liste en une chaîne de caractères.  

    Pour ce faire on utilise la méthode join sur une chaîne de caractères vide,
    ce qui donne la ligne de code suivante qui nous permet de générer un
    identifiant unique complet de 15 caractères :
    uuid = "".join(random.sample(string.digits + string.ascii_letters, 15))

    Il ne nous reste plus qu'à ajouter ce virement dans notre dictionnaire :
    self.virements[uuid] = montant

POINTS IMPORTANTS À RETENIR:
    Pour récupérer toutes les lettres de l'alphabet et tous les chiffres on 
    utilise le module string.
    Pour récupérer aléatoirement des caractères dans une chaîne de caractères,
    on utilise la fonction sample du module random.
"""