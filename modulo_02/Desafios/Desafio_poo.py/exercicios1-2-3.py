#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função:Exercícios 1, 2 e 3: 
# Classe Pessoa, Criando Pessoas e Método apresentar

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

joao = Pessoa("João", 25)
maria = Pessoa("Maria", 30)

print(f"Nome: {joao.nome}, Idade: {joao.idade}")
print(f"Nome: {maria.nome}, Idade: {maria.idade}")

joao.apresentar()
maria.apresentar()
