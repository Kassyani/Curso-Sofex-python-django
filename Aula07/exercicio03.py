'''Menu de comandos para um Robo'''

inicio = 0

while True:

    opção = input("Escolha uma opção: ")
"1- Avançar.\n"
"2- Recuar.\n"
"3 - Status\n"
"4 - Desligar.\n"

if opção == "1":
    inicio += 1
    print(f"Robô avança +1")

elif opção == "2":
    inicio -= 1
    print("")

elif opção == "3":

elif opção == "4":

else: