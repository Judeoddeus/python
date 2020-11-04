# 87: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
soma = soma2 = soma3 = maior = menor = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a [{l}, {c}]: '))
        if matriz [l][c] % 2 == 0:
            soma = soma + matriz[l][c]
print('-_-'*20)
for l in range(0 , 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-_-'*20)
print(f'A soma dos valores pares é {soma}')
for i, v in enumerate(matriz):
    soma2 += v[2]
print(f'A soma dos valores da terceira coluna é {soma2}')
print(f'A soma da segunda linha é {max(matriz[1])}')


