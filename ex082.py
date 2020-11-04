# 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas
# os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
lista = []
pares = []
impares = []
'''
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N': break
lista.sort()'''
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if res == 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Lista completa {lista}')
print(f'Lista de números pares {pares}')
print(f'Lista de números impares {impares}')
