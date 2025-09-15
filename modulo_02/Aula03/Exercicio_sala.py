#Autor: Kassyani Mênedy
#Data: 08/09/2025
#Função: Agenda de Contatos: Crie um sistema simples de agenda que use um dicionário. 
# Use um loop while para mostrar um menu com opções de "adicionar contato", "buscar contato" e "sair". 

agenda_contatos = {}

#.get() estudar

while True:
    print('Menu de opções:\n'
          'Opção 1 = Adicionar contato\n'
          'Opção 2 = Buscar contato\n'
          'opção 3 = Sair')
    
    opção = input("Escolha uma opção: ")

    if opção == '1':
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o numero de telefone do contato: ')
        agenda_contatos[nome] = telefone

    elif opção == '2':
        buscar_contato = input("Qual o nome do contato? ")
        contato = contato.get(nome, 'Contato não encontrado!')

    elif opção == '3':
        print("Até a próxima <3")
        continue
    break

