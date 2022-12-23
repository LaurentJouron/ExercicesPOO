class Animal:
    def __init__(self, nom):
        self.nom = nom

    def parle(self):
        raise NotImplementedError("Je ne sais pas quoi dire...")


class Chien(Animal):
    def parle(self):
        return "Woof!"


class Chat(Animal):
    def parle(self):
        return "Miaou!"


a = Animal("Patrick")
chat = Chat("Titi")
chien = Chien("Max")

print(chat.parle())
print(chien.parle())

"""
Surcharger une méthode - Solution

CODE:
    class Animal:
        def __init__(self, nom):
            self.nom = nom
     
        def parle(self):
            raise NotImplementedError("Je ne sais pas quoi dire...")
     
    class Chien(Animal):
        def parle(self):
            return "Woof!"
     
    class Chat(Animal):
        def parle(self):
            return "Miaou!"
     
    a = Animal("Patrick")
    chat = Chat("Titi")
    chien = Chien("Max")
     
    print(chat.parle())
    print(chien.parle())

EXPLICATIONS:
    Pour réussir cet exercice, il fallait implémenter la méthode parle pour les
    classes Animal, Chien et Chat.
    Pour la première classe, on devait lever une erreur. Pour ce faire, on 
    utilise l'instruction raise suivie du nom de l'erreur que l'on souhaite 
    lever ainsi que le message à afficher :
    class Animal:
        def __init__(self, nom):
            self.nom = nom
     
        def parle(self):
            raise NotImplementedError("Je ne sais pas quoi dire...")
    Il suffisait ensuite d'implémenter cette même méthode sur les deux autres 
    classes, en retournant la bonne chaîne de caractère selon l'animal :
    class Chien(Animal):
        def parle(self):
            return "Woof!"
          
    class Chat(Animal):
        def parle(self):
            return "Miaou!"

POINTS IMPORTANTS À RETENIR:
    Pour lever une erreur, on utilise l'instruction raise.
    Pour surcharger une méthode, il suffit de la ré-implémenter dans la classe 
    fille.
"""