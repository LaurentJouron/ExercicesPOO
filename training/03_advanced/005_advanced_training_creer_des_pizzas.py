"""
Créer des pizzas
    Quelle meilleure façon de faire de la programmation qu'en créant des
    pizzas ?
    Dans cet exercice, vous devez utiliser les méthodes de classe pour créer
    une pizza napolitaine et une pizza au fromage avec la syntaxe suivante :
    napo = Pizza.napolitaine()
    fromage = Pizza.fromage()
    La pizza napolitaine devra avoir comme nom "Napolitaine", comme ingrédients
    la liste ["Tomates", "Anchois"] et comme prix 12.99€.
    La pizza au fromage elle devra avoir comme nom "4 Fromages", comme
    ingrédients ["Mozzarella", "Comté", "Cheddar", "Gorgonzola"] et comme
    prix 14.99€.

Astuces:
    Pour utiliser une méthode de classe, il faut utiliser le décorateur
    classmethod.
"""

class Pizza:
    def __init__(self, nom, ingredients, prix=9.99):
        self.nom = nom
        self.ingredients = ingredients
        self.prix = prix

napo = Pizza.napolitaine()
fromage = Pizza.fromage()