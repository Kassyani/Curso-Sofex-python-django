from pessoas import Pessoa


class Estudante (Pessoa):

    def __init__(self, nome:str, idade:int, matricula:int):

    super().__init__(nome, idade)

    self.matricula = matricula

