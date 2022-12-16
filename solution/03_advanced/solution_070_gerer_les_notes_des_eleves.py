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