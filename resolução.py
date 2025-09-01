#Autor: Kassyani Mênedy Faria
#Data: 31/08/2025
#Função: Descobrir se os 3 números apresentados pelo usuário podem formar um triangulo.

print("Desafio do Triangulo: Vamos descobrir se os três números que você escolheu conseguem formar um triangulo?")

while True:
    ladoA_pl = input("Digite o 1° número: ")
    if not ladoA_pl.isnumeric():
        print("Inválido! Digite um número inteiro positivo.")
        continue
    ladoA = int(ladoA_pl)
    if ladoA <= 0:
        print("Inválido! O número deve ser positivo.")
        continue

    ladoB_pl = input("Digite o 2° número: ")
    if not ladoB_pl.isnumeric():
        print("Inválido! Digite um número inteiro positivo.")
        continue
    ladoB = int(ladoB_pl)
    if ladoB <= 0:
        print("Inválido! O número deve ser positivo.")
        continue

    ladoC_pl = input("Digite o 3° número: ")
    if not ladoC_pl.isnumeric():
        print("Inválido! Digite um número inteiro positivo.")
        continue
    ladoC = int(ladoC_pl)
    if ladoC <= 0:
        print("Inválido! O número deve ser positivo.")
        continue

    soma = (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB)

    diferenca = (ladoA > abs(ladoB - ladoC)) and (ladoB > abs(ladoA - ladoC)) and (ladoC > abs(ladoA - ladoB))

    if soma and diferenca:
        print("Os números podem formar um triângulo! Parabéns <3 ")
    else:
        print("Os números não formam um triângulo! Tente Novamente :( ")