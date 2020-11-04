# 90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.
# nota < 5 = reprovado / nota > 7 = aprovado nota <= 7 = recuperação
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média da {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
    dados['situacao'] = 'Recuperação'
else:
    dados['situação'] = 'Reprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}.')

