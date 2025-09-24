#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 5: Conta Bancária

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

conta = ContaBancaria("Ana", 1000)
conta.depositar(500)
