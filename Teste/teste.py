class caixa:
    def __init__(self, forma,cor,peso,tamanho,textura):
        self.forma = forma
        self.cor = cor
        self.peso = peso
        self.tamanho = tamanho
        self.textura = textura

    def armazenar(self):
        print("A caixa armazenou um objeto")

    def abrir(self):
        print("A caixa abriu")

    def fechar(self):
        print("A caixa fechou")


class Inseto(caixa):
    def __init__(self, forma,cor,peso,tamanho,textura, asa, antena):
        super().__init__(asa, antena)
        self.asa = asa
        self.antena = antena 
        

    




