#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função:Exercício 4: Molde de um Produto

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

notbook = Produto("Notbook", 15.50)
notbook = Produto("Notbook", 3.00)

print(f"Produto: {notbook.nome}, Preço: R${notbook.preco}")
print(f"Produto: {notbook.nome}, Preço: R${notbook.preco}")
