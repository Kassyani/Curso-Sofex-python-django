#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 6: Lógica no Saque


class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

conta = ContaBancaria("Ana", 1000)
conta.sacar(200)
conta.sacar(2000)
