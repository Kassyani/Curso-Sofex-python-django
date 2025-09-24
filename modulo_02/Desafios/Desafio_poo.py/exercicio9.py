#Autor: Kassyani Mênedy
#Data: 23/09/2025
#Função: Exercicio 09: Funcionários com Bônus

class Funcionario:
    percentual_bonus = 1.10 

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aplicar_bonus(self):
        self.salario *= Funcionario.percentual_bonus
        print(f"{self.nome} agora tem salário de R${self.salario:.2f}")

f1 = Funcionario("Carlos", 2000)
f2 = Funcionario("Paula", 3000)

f1.aplicar_bonus()
f2.aplicar_bonus()
