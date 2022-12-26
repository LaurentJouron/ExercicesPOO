class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self._numero = numero
        self.balance = balance

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, value):
        raise AttributeError("Vous ne pouvez pas modifier le numéro du compte.")


john = Compte(nom="John Smith", numero="123456", balance=20000)


"""
Empêcher la modification d'un attribut - Solution

    CODE:
    class Compte:
        def __init__(self, nom, numero, balance):
            self.nom = nom
            self._numero = numero
            self.balance = balance
     
        @property
        def numero(self):
            return self._numero
     
        @numero.setter
        def numero(self, value):
            raise AttributeError("Vous ne pouvez pas modifier le numéro du 
            compte.")
     
     
    john = Compte(nom="John Smith", numero="123456", balance=20000)

EXPLICATIONS:
    Pour réussir cet exercice, nous utilisons le concept de propriétés.
    La première chose à faire pour éviter une erreur de récursion, est 
    d'utiliser un attribut protégé pour le numéro, qui sera utilisé à 
    l'intérieur de notre classe. Nous appelons cet attribut self._numero:
    class Compte:
        def __init__(self, nom, numero, balance):
            self.nom = nom
            self._numero = numero
            self.balance = balance
    Nous mettons ensuite un système de 'getter' et 'setter' pour permettre 
    d'accéder et modifier cet attribut avec le nom numero.

Dans sa forme la plus basique, cela ressemblerait à ceci :

class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self._numero = numero
        self.balance = balance
 
    @property
    def numero(self):
        return self._numero
 
    @numero.setter
    def numero(self, value):
        self._numero = value
    On utilise le décorateur @property pour la fonction de 'getter' (donc pour
    récupérer l'attribut _numero avec le nom numero) et le décorateur 
    @numero.setter pour modifier l'attribut.

    Cela nous permettrait d'accéder à l'attribut numero et de le modifier sur 
    notre instance de cette façon :
    >>> john.numero
    '12345'
    >>> john.numero = '654321'
    >>> john.numero
    '654321'
    Dans ce cas-ci, nous souhaitons empêcher la modification de cet attribut.
    Nous allons donc lever une erreur avec l'instruction raise dans la 
    propriété 'setter' :
    @numero.setter
    def numero(self, value):
        raise AttributeError("Vous ne pouvez pas modifier le numéro du compte.")

POINTS IMPORTANTS À RETENIR:
    Pour mettre en place un système de 'getter' et 'setter' avec les 
    propriétés, on utilise les décorateurs @property et @attribute.setter sur 
    des méthodes.
    Pour lever une erreur, on utilise l'instruction raise suivie du nom de *
    l'erreur que l'on souhaite lever.
"""