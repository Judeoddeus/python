time = []
jogador = {}
partidas =[]
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    totPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, totPartidas):
        partidas.append(int(input(f'   Quantos gols ma partida {i + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('-- Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 40)
# código for para o cabeçalho ficar arrumado
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=' * 40)
# Código para mostrar cada jogador e seus dados (nome e gols)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')# alterra todos os dados para string.Sem isso da erro
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador(Use 999 para parar.) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse código {busca}!')
    else:
        print(f'-- LEVATAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, gol in enumerate(time[busca]['gols']): # enumerate da lista de gols
            print(f'No jogo {i+1} fez {gol} gols.')
    print('-=' * 40)
print('<<< VOLTE SEMPRE >>>')
