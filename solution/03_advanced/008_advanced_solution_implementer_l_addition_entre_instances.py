class Chemin:
    def __init__(self, chemin):
        self.chemin = chemin

    def __str__(self):
        return self.chemin

    def __add__(self, content):
        return Chemin(f"{self.chemin}/{content}")


c = Chemin("/Users/john")
composite = f"{c}dossiertestscript"
print(composite)


"""
Implémenter l'addition entre instances - Solution

CODE:
    class Chemin:
        def __init__(self, chemin):
            self.chemin = chemin
     
        def __str__(self):
            return self.chemin
     
        def __add__(self, content):
            return Chemin(self.chemin + "/" + content)

    c = Chemin("/Users/john")
    composite = c + "dossier" + "test" + "script"
    print(composite)

EXPLICATIONS:
    Pour implémenter l'addition entre instances, on utilise la méthode 
    spéciale __add__.
    Cette méthode est appelée quand on utilise le symbole d'addition après une
    instance de notre classe.
    Cette méthode prend un paramètre qui va récupérer ce qui est envoyée après
    le symbole d'addition. 
    Ainsi, le code suivant :
    c = Chemin("/Users/john")
    composite = c + "dossier"
    Revient à faire :
    c = Chemin("/Users/john")
    c.__add__("dossier")
    À l'intérieur de cette méthode __add__ nous ajoutons donc l'argument 
    content à notre attribut chemin en ajoutant un slash entre les deux :
    def __add__(self, content):
        return self.chemin + "/" + content
    Le problème c'est que si on s'arrête là en retournant directement une 
    chaîne de caractères, on ne pourra additionner qu'une seule chaîne de 
    caractères avec notre instance.
    Pour remédier à cela et permettre d'ajouter autant de chaînes de caractères
    à notre instance, il faut à la place retourner une instance de la classe 
    Chemin elle-même :
    def __add__(self, content):
        return Chemin(self.chemin + "/" + content)
    C'était la petite subtilité de l'exercice. Bravo si vous l'avez réussi 
    sans regarder la solution !

POINTS IMPORTANTS À RETENIR:
    Pour permettre l'addition entre différentes instances d'une classe, on 
    implémente la méthode __add__.
    Pour permettre d'utiliser l'opérateur d'addition en chaîne, on retourne 
    une instance de la classe elle-même.
"""