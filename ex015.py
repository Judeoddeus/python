# 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quanto Km rodados? '))
dias = int(input('Quantos dias alugados? '))
apagar = (km * 0.15) + (dias * 60)
print(f'O total a pagar é de R${apagar:.2f}')
