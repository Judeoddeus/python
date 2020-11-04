# 92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o
# (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
dados = {}

dados['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['carteira de trabalho'] = int(input('Carteira de trabalho [0 não tem]: '))
if dados['carteira de trabalho'] != 0:
    dados['ano de contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário R$'))
    dados['aposentadoria'] = (dados['ano de contratacao'] + 35) - nasc
print('-='*30)
for k, v in dados.items():
    print(f'- {k} tem valor {v}')
