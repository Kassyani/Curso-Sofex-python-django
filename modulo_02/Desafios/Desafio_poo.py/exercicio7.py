#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 7: Calculadora de Retângulos


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

ret = Retangulo(5, 3)
print("Área:", ret.calcular_area())
print("Perímetro:", ret.calcular_perimetro())
