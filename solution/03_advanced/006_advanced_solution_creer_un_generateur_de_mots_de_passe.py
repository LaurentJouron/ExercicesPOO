import string
import random


class PasswordGenerator:

    @staticmethod
    def generate(length):
        return "".join(random.sample(string.digits + string.ascii_letters, length))


mot_de_passe = PasswordGenerator.generate(15)

"""
Créer un générateur de mots de passe - Solution

CODE:
    import string
    import random
     
    class PasswordGenerator:
        @staticmethod
        def generate(length):
            return "".join(random.sample(string.digits + string.ascii_letters, length))
                
    mot_de_passe = PasswordGenerator.generate(15)

EXPLICATIONS:
    Un exercice assez court à mettre en place mais qui faisait appel à 
    plusieurs notions.
    Premièrement, nous devions créer une méthode qui soit utilisable 
    directement par la classe.
    Pour cela, on utilise le décorateur @staticmethod qui permet de créer une
    méthode statique.
    On créait donc une méthode generate qui acceptait un seul paramètre que 
    l'on a appelé ici length et qui permettait de définir la longueur du mot de
    passe:
    @staticmethod
    def generate(length):
    Ensuite, nous utilisons le module string pour récupérer toutes les lettres
    de l'alphabet en majuscules et minuscules et tous les chiffres de 0 à 9 :
    string.digits + string.ascii_letters
    Il ne nous restait plus qu'à retourner un échantillon aléatoire de la 
    longueur indiquée par le paramètre length grâce à la fonction sample du 
    module random.
    La fonction sample nous retournant une liste, il ne fallait pas oublier de
    joindre les éléments de la liste avec la méthode join, sur une chaîne de 
    caractères vide:
    return "".join(random.sample(string.digits + string.ascii_letters, length))

POINTS IMPORTANTS À RETENIR:
    Pour créer une méthode que l'on peut utiliser directement sur une classe, 
    on utilise les méthodes statiques et le décorateur @staticmethod.
    Pour générer un échantillon aléatoire d'une certaine longueur, on utilise
    la méthode sample du module random.
"""