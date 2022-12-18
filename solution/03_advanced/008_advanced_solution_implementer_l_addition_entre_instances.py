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
