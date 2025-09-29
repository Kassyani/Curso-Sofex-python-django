#Autor: Kassyani Mênedy
#Data: 29/09/2025
#Função: Ligar um carro

class Motor:
    def __init__(self):
        pass

    def ligar(self):
        print("O motor ligou...")

class Carro:
    def __init__(self):
        self.motor = Motor()
        
    def ligar_carro(self):

        self.motor.ligar()

carrinho= Carro()
carrinho.ligar_carro()