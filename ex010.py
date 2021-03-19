# 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
dinheiro = float(input('Quanto dinheiro você tem? '))
dolar = dinheiro / 5.55
print(f'Você tem R${dinheiro:.2f} e isso vale U$ {dolar:.2f}')



