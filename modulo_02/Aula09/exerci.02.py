#Autor: Kassyani Mênedy
#Data: 29/09/2025
#Função: Criar uma cafeteria

class GraoDeCafe:
    def __init__(self):
        pass
    def moer(self):
        print("Os grãos de café foram moídos.")

class Agua:
    def __init__(self):
        pass
    def aquecer(self):
        print("A água está aquecida.")



class Cafeteria:
    def __init__(self):
        self.grao = GraoDeCafe()
        self.agua = Agua()

    def preparar_cafe(self):
        self.grao.moer()
        self.agua.aquecer()


cafeteria = Cafeteria()

cafeteria.preparar_cafe()







        


grao = GraoDeCafe()
agua = Agua()

cafeteria = Cafeteria(grao, agua)

cafeteria.preparar_cafe()