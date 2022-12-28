class Note:
    def __init__(self, valeur):
        self.valeur = valeur

    def __repr__(self):
        return f"{str(self.valeur)} / 20"


class Notes(list):
    def ajouter_note(self, note):
        self.append(note)

    def notes_parfaites(self):
        return sum(note.valeur == 20 for note in self)

    def moyenne(self):
        return round(sum(note.valeur for note in self) / len(self), 1)


valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
notes = Notes()

for valeur_note in valeur_notes:
    notes.ajouter_note(note=Note(valeur=valeur_note))

print(notes.notes_parfaites())
print(notes.moyenne())

"""
Gérer les notes d'élèves - Solution

CODE:
    class Note:
        def __init__(self, valeur):
            self.valeur = valeur
     
        def __repr__(self):
            return "{} / 20".format(str(self.valeur))

    class Notes(list):
        def ajouter_note(self, note):
            self.append(note)
     
        def notes_parfaites(self):
            nombre = 0
            for note in self:
                if note.valeur == 20:
                    nombre += 1    
            return nombre
     
        def moyenne(self):
            return round(sum([note.valeur for note in self]) / len(self), 1)

    valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
    notes = Notes()
     
    for valeur_note in valeur_notes:
        notes.ajouter_note(note=Note(valeur=valeur_note))
     
    print(notes.notes_parfaites())
    print(notes.moyenne())

EXPLICATIONS:
    La première chose à faire était de créer une classe Note qui permette de 
    représenter la note d'un étudiant.
    Cette classe devait posséder comme attribut la valeur de la note.
    On récupère donc cette valeur au moment de l'instanciation de la classe, 
    dans la méthode __init__ :
    
    class Note:
        def __init__(self, valeur):
            self.valeur = valeur
    On devait également modifier la représentation de la classe pour qu'elle 
    affiche la valeur de la note sur 20.
    Pour cela, on implémente la méthode __repr__ :
    def __repr__(self):
        return "{} / 20".format(str(self.valeur))
    On devait ensuite créer une classe Notes qui permette d'ajouter et 
    récupérer des informations sur toutes les notes de notre liste.
    On devait faire hériter notre classe de la classe list afin de pouvoir 
    ajouter des notes directement dans les instances de cette classe avec la 
    méthode ajouter_note :
    class Notes(list):
        def ajouter_note(self, note):
            self.append(note)
    Comme vous pouvez le voir dans le code ci-dessus, le fait d'hériter de la
    classe list nous permet d'ajouter les notes directement avec self.append,
    car les instances créées à partir de la classe Notes seront des listes (on 
    peut donc ajouter des éléments à l'intérieur avec la méthode append).
    Pour finir, il suffisait d'implémenter deux méthodes pour récupérer toutes 
    les notes égales à 20 (la méthode notes_parfaites) et la moyenne des notes
    (la méthode moyenne):
    def notes_parfaites(self):
        nombre = 0
        for note in self:
            if note.valeur == 20:
                nombre += 1
        return nombre
     
    def moyenne(self):
        return round(sum([note.valeur for note in self]) / len(self), 1)
    Rien de bien compliqué à l'intérieur de ces deux méthodes, il s'agit juste 
    de vérifier les notes égales à 20 et de faire la moyenne des instances de 
    la classe Note contenues dans notre liste avec la fonction sum.
    Vous remarquerez que comme notre instance est une liste, on peut boucler 
    sur les éléments de l'instance tout simplement en bouclant sur self avec 
    for note in self.

POINTS IMPORTANTS À RETENIR:
    Pour hériter d'une classe, on met le nom de la classe dans les parenthèses
    lors de la définition de notre classe.
    Pour changer la représentation d'une classe, on utilise la méthode __repr__.
    Quand on hérite d'une classe, on hérite de toutes ses méthodes.
    En héritant de la classe list, on peut donc utiliser la méthode append.
"""