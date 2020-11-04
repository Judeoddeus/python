# 84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp, dados = [], []
maior = menor = nome_maior = nome_menor = 0
while True:
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    dados.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N': break
print(f'Ao todo, você cadastrou {len(dados)}')
print(f'O maior peso é {maior}Kg. o peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso é {menor}Kg. O peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
