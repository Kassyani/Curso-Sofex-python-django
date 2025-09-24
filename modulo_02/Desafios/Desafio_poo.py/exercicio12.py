#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 12: Representação Amigável (str)


class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f"Filme: '{self.titulo}' ({self.ano}) - Diretor: {self.diretor}"

filme = Filme("Bonequinha de Luxo", "Truman Capote", 1961)
print(filme)
