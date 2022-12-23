"""
Surcharger une méthode:
    Dans cet exercice, vous devez implémenter la méthode parle pour les classes
    Animal, Chien et Chat.
    Dans le cas de la classe Animal, la méthode parle doit lever une erreur de
    type NotImplementedError avec le message d'erreur "Je ne sais pas quoi
    dire...".
    Dans le cas de la classe Chien, vous devez surcharger la méthode parle
    pour qu'elle retourne la chaîne de caractères "Woof!".
    Pour la classe Chat, la méthode parle doit retourner la chaîne de
    caractères "Miaou!".
Surcharger une méthode
    Dans cet exercice, vous devez implémenter la méthode parle pour les classes
    Animal, Chien et Chat.
    Dans le cas de la classe Animal, la méthode parle doit lever une erreur de
    type NotImplementedError avec le message d'erreur "Je ne sais pas quoi dire...".
    Dans le cas de la classe Chien, vous devez surcharger la méthode parle pour
    qu'elle retourne la chaîne de caractères "Woof!".
    Pour la classe Chat, la méthode parle doit retourner la chaîne de
    caractères "Miaou!".

Astuces:
    Pour lever une erreur, on utilise l'instruction raise.
"""


class Animal:
    def __init__(self, nom):
        self.nom = nom


class Chien(Animal):
    pass


class Chat(Animal):
    pass


a = Animal("Patrick")
chat = Chat("Titi")
chien = Chien("Max")

print(chat.parle())
print(chien.parle())