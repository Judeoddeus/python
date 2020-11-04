#94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
# pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média
cadastro = {}
listaDeDados = []
soma = media = 0
while True:
    cadastro['nome'] = str(input('Nome: ')).strip()
    # Valida o sexo em F ou M mostrando mensagem de erro.
    while True:
        cadastro['sexo'] = str(input('Sexo - [F/M]: ')).strip().upper()[0]
        if cadastro['sexo'] in 'FM':
            break
        print('ERRO! Responda apenas F ou M.')
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    listaDeDados.append(cadastro.copy())
    resp = ' '
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-*' * 30)
print(f'A) Ao todo temos {len(listaDeDados)} pessoas cadastradas.')
media = soma / len(listaDeDados)
print(f'B) A média de idade é {media:5.2f} de anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
# Checar dentro da lista as pessoas com o mesmo sexo (F) e trazer apenas os nomes.
for mulher in listaDeDados:
    if mulher['sexo'] == 'F':
        print(f' {mulher["nome"]}...', end='')
print()
# Verificar as pessoas que tem idade acima da média.
print('D) Lista das pessoas que estão acima da média:')
for i, v in enumerate(listaDeDados):
    if v['idade'] >= media:
        print(f'     nome = {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]};')
print('<< ENCERRADO >>')
'''Pode usar como segunda opção.

for i, v in enumerate(listaDeDados):
    if v['idade'] >= media:
    print('   ', end='')
    for k, v in cadastro.items():
        print(f'{k} = {v};', end='')
    print()

'''