class MachineACafe:
    def __init__(self):
        self.temperature_eau = 0

    def __chauffe_eau(self):
        self.temperature_eau = 100
        print("L'eau est chaude.")

    def __moud_cafe(self):
        print("Café moulu avec succès.")

    def fait_du_cafe(self):
        self.__moud_cafe()
        self.__chauffe_eau()
        print("Le café est prêt")


machine = MachineACafe()
machine.fait_du_cafe()

"""
Rendre une méthode privée - Solution

CODE:
    class MachineACafe:
        def __init__(self):
            self.temperature_eau = 0
     
        def __chauffe_eau(self):
            self.temperature_eau = 100
            print("L'eau est chaude.")
     
        def __moud_cafe(self):
            print("Café moulu avec succès.")
     
        def fait_du_cafe(self):
            self.__moud_cafe()
            self.__chauffe_eau()
            print("Le café est prêt")

    machine = MachineACafe()
    machine.fait_du_cafe()

EXPLICATIONS;
    Rien de compliqué dans cet exercice si vous connaissiez les méthodes
    privées.
    Pour valider le code, il suffisait de transformer les méthodes chauffe_eau
    et moud_cafe en méthodes privées.
    Pour ce faire, il suffit d'ajouter deux tirets du bas avant le nom des
    méthodes.
    Il ne fallait pas oublier de modifier l'appel à ces méthodes dans la
    méthode fait_du_cafe pour appeler les méthodes privées :
    def fait_du_cafe(self):
        self.__moud_cafe()
        self.__chauffe_eau()
        print("Le café est prêt")
    En rendant ces méthodes privées, on ne peut plus les appeler directement
    depuis l'instance machine :
    >>> machine.__moud_cafe()
    AttributeError: 'MachineACafe' object has no attribute '__moud_cafe'

POINTS IMPORTANTS À RETENIR:
    Pour rendre une méthode privée, il suffit de la précéder de deux tirets du
    bas.
"""