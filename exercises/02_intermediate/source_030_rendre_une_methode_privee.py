class MachineACafe:
    def __init__(self):
        self.temperature_eau = 0

    def chauffe_eau(self):
        self.temperature_eau = 100
        print("L'eau est chaude.")

    def moud_cafe(self):
        print("Café moulu avec succès.")

    def fait_du_cafe(self):
        self.moud_cafe()
        self.chauffe_eau()
        print("Le café est prêt")


machine = MachineACafe()
machine.fait_du_cafe()