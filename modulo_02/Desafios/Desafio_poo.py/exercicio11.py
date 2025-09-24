#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 11: Biblioteca de Livros

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def listar_livros(self):
        for livro in self.acervo:
            print(f"{livro.titulo} - {livro.autor}")

bib = Biblioteca()
l1 = Livro("Dom Casmurro", "Machado de Assis")
l2 = Livro("O Hobbit", "J.R.R. Tolkien")

bib.adicionar_livro(l1)
bib.adicionar_livro(l2)
bib.listar_livros()
