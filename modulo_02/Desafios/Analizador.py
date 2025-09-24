#Autor: Kassyani Mênedy 
#Data: 15/09/2025
#Função: Analisador de Frases 
# Crie um programa que recebe uma frase do usuário e faz uma análise completa sobre ela, 
#Mostrando: 
#A quantidade de palavras na frase. 
# A quantidade de vogais (a, e, i, o, u). 
#A quantidade de consoantes. 
#Se a frase é um palíndromo (ou seja, se ela pode ser lida da mesma forma de trás para 
#frente, ignorando espaços e letras maiúsculas). 
#Exemplo de Execução: 
#Digite uma frase para analisar: A sacada da casa --- Resumo da Análise --- 
# Palavras: 4 Vogais: 6 Consoantes: 6 É um palíndromo? Sim

frase = input("Digite uma frase para analisar: ")
frase_limpa = frase.lower().replace(" ", "")

palavras = frase.split()
quant_palavras = len(palavras)

vogais = "aeiou"
qtd_vogais = 0
qtd_consoantes = 0

for letra in frase_limpa:
    if letra.isalpha():
        if letra in vogais:
            qtd_vogais += 1
        else:
            qtd_consoantes += 1

if frase_limpa == frase_limpa[::-1]:
    palindromo = "Sim"
else:
    palindromo = "Não"

print("\n--- Resumo da Análise ---")
print(f"Palavras: {quant_palavras}")
print(f"Vogais: {qtd_vogais}")
print(f"Consoantes: {qtd_consoantes}")
print(f"É um palíndromo? {palindromo}")