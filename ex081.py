# 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*30)
print(f'Você digitou {c} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem descrescente são {numeros}')
print(f'O valor 5 faz parte da lista' if 5 in numeros else "O valor 5 não faz parte da lista")
