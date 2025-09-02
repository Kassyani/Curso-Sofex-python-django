#Autor: Kassyani Mênedy
#Data: 04/08/2025
#Função: Conversor de Moedas Simples (Variáveis e input):
# ○ Crie um programa que peça ao usuário o valor em reais (float).
# ○ Calcule o valor equivalente em dólar, sabendo que 1 dólar = R$ 5,00.
# ○ Imprima o resultado.

#Variaveis
dinheiro = float(input("Digite o valor em R$: "))
dolar = 5.00
valor = dinheiro/dolar

#Função
print(f"Seu valor em dólars fica: {valor:.2f}")
