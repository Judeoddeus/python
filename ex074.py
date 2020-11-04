from random import randint

num_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for n in num_aleatorios:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(num_aleatorios)}')
print(f'O menor valor sorteado foi {min(num_aleatorios)}')
