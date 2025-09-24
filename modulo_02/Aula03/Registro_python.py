#Autor: Kassyani Mênedy Faria
#Data: 08/09/2025
#Função: analisar dados de acessos dos usuarios

#variaveis
registros_acessos = []
usuarios_sucesso = set()
tempo_total_sucesso = 0

#Comandos
while True:
    usuario = input("Digite o nome de usuário (ou 'parar' para sair): ")
    if usuario == "parar":
        break

    print("Selecione o status:\n1 - Sucesso\n2 - Falha")
    opcao = input("Opção: ")

    if opcao not in ("1", "2"):
        print("Opção inválida! Digite 1 ou 2.")
        continue

    status = "sucesso" if opcao == "1" else "falha"

    try:
        duracao = int(input("Digite a duração da sessão em minutos: "))

    except ValueError:

        print("Duração inválida! Registro descartado.")
        continue

    registros_acessos.append((usuario, status, duracao))
    if status == "sucesso":
        usuarios_sucesso.add(usuario)
        tempo_total_sucesso += duracao

print("\nRegistros de acessos:")
print(registros_acessos)

print("\nUsuários com acesso bem-sucedido:")
print(usuarios_sucesso)

print("\nTempo total das sessões bem-sucedidas:", tempo_total_sucesso, "minutos")

