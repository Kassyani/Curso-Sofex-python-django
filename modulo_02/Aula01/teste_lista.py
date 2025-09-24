cores = ['azul','verde','amarelo' ]
cor = input('Escolha a cor que você quer remover: ').lower()
cores.remove(cor)
print(f'A lista de cores atual é:{cores}')