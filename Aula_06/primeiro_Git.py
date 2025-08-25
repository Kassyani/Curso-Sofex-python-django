"""""""""""
Programa de Banco
1- rodar em Loop infinito
2- ter conta e senha (validar)
3- encerrar atendimento
4- cheque especial (limite saldo negativo)
5- tentar 3 vezes a senha
6- opções (saque,deposito, saldo)
7- mostrar saldo apos saque
8- alterar senha
9- dizer: o nome do usuario
10- pagar boleto
"""""""""
#Variaves

conta_corrente = "123456-7"
senha_usuario = "54321"
saldo = 0
limite_saldo_negativo = 500
nome_usuario = "José"

while True:
    for i in ranger(3):
        conta = input("Entre com a sua Conta orrente: ")
        senha = input("Entre com a sua senha: ")
        if conta == conta_corrente and senha == senha_usuario:
            print(f"Bem-vindo {nome_usuario}!")
            acesso_permitido = True
            break
        else:
            print("Conta ou senha Inválida")
            acesso_permitido = False
            
        if not acesso_permitido:
            break

    while True:
    opcaoput("Escolha uma opção:?\n")
    "1- Ver saldo.\n"\
    "2- Sacar valor.\n"\
    "3- Depositar.\n"\
    "4- Pagar Boleto.\n"\
    "5- Alterar senha.\n"\
    "6- Sair.\n"\
    
if opção == "1":
        print(f"Seu Saldo atual é de {saldo_atual}.")
elif opção == '2':
        valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
if valor_a_sacar <= (saldo_atual + limite_saldo_negativo):
        saldo += valor_a_sacar
        print("Saldo liberado, retire seu valor!")
else:
        print("Saldo insufuciente!")

     elif opção =='3':

depositar = float(input("insira o valor a ser depositado: "))
    
if depositar > 0:
        saldo += depositar
    else:
        print("Valor invalido!")
    elif opção =='4':
boleto = float(input("Insira o valor do boleto: "))
if bole < (saldo_atual + limite_saldo_negativo):
            saldo -= boleto
        else:
            print("Saldo insufuciente")

    elif opção =='5':
        senha_antiga = input ("Digite sua senha antiga: ")
        senha_nova1 = input ("Digite sua senha nova: ")
        senha_nova02 = input("Repta sua senha nova: ")
        if senha_antiga == senha_usuario and senha_nova01 == senha_nova2:
            senha_usuario = senha_nova01
            print("Senha atualizada com sucesso!")
        else:
       print("Senha invalidá")

    elif opção =='6':
        print("Atendimento Finalizado")
        break
else:
    print("Opção Invalida")