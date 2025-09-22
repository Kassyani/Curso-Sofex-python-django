class Circulo:
    def __init__(self, raio: float):
        self._raio = raio

    @property
    def raio(self):
        return self._raio
    @raio.setter
    def raio(self, novo_raio: float):
        if novo_raio > 0:
            self._raio = novo_raio
        else:
            print()
        
    def calcular_area(self):
        area = 3.14 * self.raio ** 2
        print(area)
    
roda = Circulo(6)

roda.calcular_area()