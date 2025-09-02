#Autor: Kassyani Mênedy
#Data: 04/08/2025
#Função: Par ou Ímpar (Operadores e if-else):
# ○ Peça ao usuário para digitar um número inteiro.
# ○ Use o operador de módulo (%) para verificar se o número é par (o resto dadivisão por 2 é 0).
# ○ Imprima se o número é "Par" ou "Ímpar".

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"Esse número {numero} é Par: ")
else:
    print(f"Esse número {numero} é Ímpar: ")