# 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
# usuário vai continuar ou não. No final, mostre:
totcompra = totpreco = menorproduto = menorpreco = cont = 0
while True:
    nome_produto = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Peço: R$'))
    cont += 1
    totcompra += preco
    if preco > 1000:
        totpreco += 1
    if cont == 1 or preco < menorpreco: # simplificando
        menorpreco = preco
        menorproduto = nome_produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de R${totcompra:.2f}')
print(f'Temos {totpreco} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi a {menorproduto} que custa R${menorpreco:.2f}')
