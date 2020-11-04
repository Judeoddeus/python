# 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar
# as notas de cada aluno individualmente.
temp, ficha = [], []
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota [1]: '))
    nota2 = float(input('Nota [2]: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N': break
    print('-' * 30)
print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, v in enumerate(ficha):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')
print('-' * 30)
while True:
    mostrar = int(input(f'Mostrar notas do aluno? [999 para interromper] '))
    if mostrar == 999:
        print('Finalizando...')
        break
    for i, v in enumerate(ficha):
        if mostrar == i:
            print(f'Notas de {v[0]} são {v[1]}')
    #if mostrar <= len(ficha) - 1:
        #print(f'Notas de {ficha[mostrar][0]} são {ficha[mostrar][1]}')
print('<<<<<<< VOLTE SEMPRE >>>>>>>')
