# 85: Crie um programa onde o usuário possa digitar sete valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.
total = [[], []]
n = 0
for c in range(1, 8):
    n = (int(input(f'Digite {c}º número: ')))
    if n % 2 == 0:
        total[0].append(n)
    else:
        total[1].append(n)
total[0].sort()
total[1].sort()
print('-'*30)
print(f'Os valores pares são {total[0]}')
print(f'Os valores impares são {total[1]}')


