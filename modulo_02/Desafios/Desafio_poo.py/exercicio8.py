#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 8: Um Carro que Anda

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.nivel_combustivel = 0

    def abastecer(self, litros):
        self.nivel_combustivel += litros
        print(f"Abastecido {litros}L. Combustível atual: {self.nivel_combustivel}L")

    def dirigir(self, distancia):
        consumo = distancia / 10 
        if consumo <= self.nivel_combustivel:
            self.nivel_combustivel -= consumo
            print(f"O carro {self.modelo} andou {distancia}km.")
        else:
            print("Não há combustível suficiente.")

carro = Carro("Fusca")
carro.abastecer(5)
carro.dirigir(30)
carro.dirigir(50)
