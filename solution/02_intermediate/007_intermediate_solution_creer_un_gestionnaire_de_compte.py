class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance

    def deposer(self, montant):
        self.balance += montant

    def retirer(self, montant):
        self.balance -= montant


compte_john = Compte(nom="John", numero="12345", balance=20000)
compte_john.deposer(montant=3000)
compte_john.retirer(montant=200)

"""
Créer un gestionnaire de compte - Solution

CODE:    
    class Compte:
        def __init__(self, nom, numero, balance):
            self.nom = nom
            self.numero = numero
            self.balance = balance
     
        def deposer(self, montant):
            self.balance += montant
     
        def retirer(self, montant):
            self.balance -= montant
    compte_john = Compte(nom="John", numero="12345", balance=20000)
    compte_john.deposer(montant=3000)
    compte_john.retirer(montant=200)

EXPLICATIONS:
    La première chose à faire était de créer la classe Compte ainsi que sa 
    méthode __init__ afin de pouvoir créer une instance avec les bons 
    attributs:
    
    class Compte:
        def __init__(self, nom, numero, balance):
            self.nom = nom
            self.numero = numero
            self.balance = balance
    Cela nous permet ainsi de créer l'instance compte_john :    
    compte_john = Compte(nom="John", numero="12345", balance=20000)
    Il fallait ensuite créer deux méthodes deposer et retirer qui nous permette
    de modifier l'attribut balance :
    
    def deposer(self, montant):
        self.balance += montant
     
    def retirer(self, montant):
        self.balance -= montant
    On utilise ici le raccourci += et -= pour rapidement incrémenter et 
    décrémenter la valeur de l'attribut balance du montant passé en argument 
    au paramètre montant.
    
    Cela revient au même que de faire :
    def deposer(self, montant):
        self.balance = self.balance + montant
     
    def retirer(self, montant):
        self.balance = self.balance - montant

POINTS IMPORTANTS À RETENIR:
    Pour créer une classe on utilise l'instruction class.
    Pour initialiser une instance, on utilise la méthode __init__.
    Pour rapidement incrémenter ou décrémenter une variable, on peut utiliser
    += ou -=.
"""