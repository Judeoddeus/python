# 95: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time = []
listaDeGosls = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    qtsPartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(0, qtsPartidas):
        listaDeGosls.append(int(input(f'   Quantos gols ma partida {i + 1}? ')))
    jogador['gols'] = listaDeGosls[:]
    jogador['total'] = sum(listaDeGosls)
    time.append(jogador.copy())
    listaDeGosls.clear()
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
for k, v in enumerate(time):# contagem de jogadores
    print(f'{k:>4}', end='')
    for dado in v.values():# mostra os dados de cada jogador (nome e gols).
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)
while True:
    posicao = int(input('Mostrar dados de qual jogador? (999 Use para parar) '))
    if posicao == 999:
        break
    if posicao >= len(time):
        print(f'ERRO! Não existe jogador com código {posicao}')
    for i, v in enumerate(time):
        if posicao == i:
            print(F'-- LEVANTAMENTO DO JOGADOR {v["nome"]}: ')
            for c in range(len(v['gols'])):
                print(f'  No jogo {c + 1} fez {v["gols"][c]} gols.')

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

