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
"""

# Variáveis
conta_corrente = "19554295707"
senha_usuario = "264080"
saldo = 0
limite_saldo_negativo = 500
nome_usuario = "Kassyani Mênedy"

while True:

    acesso_permitido = False
    for i in range(3):
        conta = input("Entre com a sua Conta Corrente: ")
        senha = input("Entre com a sua senha: ")
        if conta == conta_corrente and senha == senha_usuario:
            print(f"\nBem-vindo {nome_usuario}!\n")
            acesso_permitido = True
            break
        else:
            print("Conta ou senha inválida.\n")
    
    if not acesso_permitido:
        print("Número máximo de tentativas atingido. Encerrando atendimento.\n")
        break


    while True:
        print("\nEscolha uma opção:")
        print("1 - Ver saldo")
        print("2 - Sacar valor")
        print("3 - Depositar")
        print("4 - Pagar Boleto")
        print("5 - Alterar senha")
        print("6 - Encerrar atendimento")
        
        opcao = input("Digite sua opção: ")

        if opcao == "1":
            print(f"Seu saldo atual é de R$ {saldo:.2f}")
        
        elif opcao == "2":
            valor_a_sacar = float(input("Entre com o valor a ser sacado: "))
            if valor_a_sacar <= (saldo + limite_saldo_negativo):
                saldo -= valor_a_sacar
                print(f"Saque realizado com sucesso! Seu novo saldo é R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente!")

        elif opcao == "3":
            depositar = float(input("Insira o valor a ser depositado: "))
            if depositar > 0:
                saldo += depositar
                print(f"Depósito realizado com sucesso! Seu novo saldo é R$ {saldo:.2f}")
            else:
                print("Valor inválido!")

        elif opcao == "4":
            boleto = float(input("Insira o valor do boleto: "))
            if boleto <= (saldo + limite_saldo_negativo):
                saldo -= boleto
                print(f"Boleto pago com sucesso! Seu novo saldo é R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente para pagar o boleto.")

        elif opcao == "5":
            senha_antiga = input("Digite sua senha antiga: ")
            if senha_antiga == senha_usuario:
                senha_nova1 = input("Digite sua nova senha: ")
                senha_nova2 = input("Repita sua nova senha: ")
                if senha_nova1 == senha_nova2:
                    senha_usuario = senha_nova1
                    print("Senha atualizada com sucesso!")
                else:
                    print("As senhas não conferem.")
            else:
                print("Senha antiga incorreta.")

        elif opcao == "6":
            print("Atendimento finalizado. Obrigado por usar nosso banco!")
            break

        else:
            print("Opção inválida! Tente novamente.")

    break 