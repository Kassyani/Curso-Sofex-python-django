
'''Simulação Pedido de lanchonete'''

hamburguer = 20.00
desconto = 5.00
codigo_de_desconto = "burger05"

print("Bem-vindo à lanchonete Burguer!")

while True:
   lanche = input("Digite o nome do lanche: ")
   if lanche == "hamburguer":
       print(f"Pedido confirmado")
       break
   else:
       print("Lanche não disponível. Tente novamente!")

   cupom = input("Digite um cupom de desconto: ")
   if cupom == codigo_de_desconto:
     print(f"Seu lanche com desconto R$ {hamburguer - desconto}")
   else:
       print(f"Valor do hambúrguer sem desconto é: R$ {hamburguer}")
       