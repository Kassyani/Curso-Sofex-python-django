#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 10: Um Objeto Dentro de Outro


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.modelo = modelo
        self.motor = Motor(potencia_motor)

    def exibir_potencia(self):
        print(f"O carro {self.modelo} tem motor de {self.motor.potencia} cavalos.")

carro = Carro("Civic", 150)
carro.exibir_potencia()
