"""
Éviter la répétition avec l'héritage
    Dans cet exercice, vous devez simplifier le code grâce à l'héritage.
    En effet, dans l'état actuel du script, on répète plusieurs fois les
    informations de nom et prenom de nos personnages.
    Ça fonctionne, mais ce n'est pas très efficace.
    Vous devez donc créer une classe Personnage dont vont hériter les classes
    Magicien, Gobelin et Chevalier.
    Cette classe Personnage devra définir les attributs nom et prenom qui sont
    communs aux trois classes.
    Vous ne devez pas toucher à l'attribut puissance des classes Magicien,
    Gobelin et Chevalier.
    Ces trois classes devront donc avoir un attribut puissance égal
    respectivement à 80, 20 et 70.
Astuces:
    Pour hériter d'une classe, il faut mettre le nom de la classe entre les
    parenthèses dans la définition de votre classe.
    Par exemple class MaClasse(Parent).
"""
class Magicien:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        self.puissance = 80


class Gobelin:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        self.puissance = 20


class Chevalier:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        self.puissance = 70