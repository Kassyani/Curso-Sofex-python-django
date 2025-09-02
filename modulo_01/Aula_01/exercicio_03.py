#Autor: Kassyani Mênedy
#Data: 04/08/2025
#Função: Maior de Idade (Aninhamento de if):
# ○ Peça ao usuário o nome e a idade.
# ○ Se a idade for maior ou igual a 18, imprima Você é maior de idade."
# ○ Se for menor, imprima Você é menor de idade."

nome = input("Digite seu primeiro nome: ")


while True:
    idade = int(input("Digite sua idade: "))
    
    if idade <= 0 or idade >= 200:
        print("Digite uma idade válida!")
        continue #não está funcioonando para solicitar novamente a idade dentr d loop
    
    if idade >= 18:
        print(f"Parabéns {nome}, Você é maior de idade! ")
    else:
        print(f"Desculpe {nome}, Você não é  maior de idade! ")
    break