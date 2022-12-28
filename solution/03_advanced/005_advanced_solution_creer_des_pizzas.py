class Pizza:
    def __init__(self, nom, ingredients, prix=9.99):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

    @classmethod
    def napolitaine(cls):
        return cls(nom="Napolitaine",
                   ingredients=["Tomates", "Anchois"],
                   prix=12.99)

    @classmethod
    def fromage(cls):
        return cls(nom="4 Fromages",
                   ingredients=["Mozzarella", "Comté", "Cheddar", "Gorgonzola"],
                   prix=14.99)


napo = Pizza.napolitaine()
fromage = Pizza.fromage()


"""
Créer des pizzas - Solution

CODE:
    class Pizza:
        def __init__(self, nom, ingredients, prix=9.99):
            self.nom = nom
            self.ingredients = ingredients
            self.prix = prix
     
        @classmethod
        def napolitaine(cls):
            return cls(nom="Napolitaine",
                       ingredients=["Tomates", "Anchois"],
                       prix=12.99)
     
        @classmethod
        def fromage(cls):
            return cls(nom="4 Fromages",
                       ingredients=["Mozzarella", "Comté", "Cheddar", "Gorgonzola"],
                       prix=14.99)
     
    napo = Pizza.napolitaine()
    fromage = Pizza.fromage()
    
EXPLICATIONS:
    Pour créer des méthodes de classe, on utilise le décorateur @classmethod.
    Cela permet de créer une méthode qui possède en premier paramètre la classe
    elle-même, dans un paramètre que l'on appelle par convention cls (mais on 
    pourrait l'appeler autrement, ce n'est pas une obligation).
    Cela nous permet de retourner une instance de la classe directement dans la
    méthode, ce que nous faisons pour créer une instance de pizza 4 fromages
    avec la méthode fromage et une pizza napolitaine avec la méthode 
    napolitaine:
    @classmethod
    def napolitaine(cls):
        return cls(nom="Napolitaine",
                   ingredients=["Tomates", "Anchois"],
                   prix=12.99)

    @classmethod
    def fromage(cls):
        return cls(nom="4 Fromages",
                   ingredients=["Mozzarella", "Comté", "Cheddar", "Gorgonzola"],
                   prix=14.99)
    Il suffisait d'entrer les bonnes valeurs pour le nom, les ingrédients et 
    le prix pour valider l'exercice.
    
POINTS IMPORTANTS À RETENIR:
    Pour créer des méthodes de classe, on utilise le décorateur @classmethod.
    Le nom du premier paramètre pour les méthodes de classe s'appelle par 
    convention cls.
"""