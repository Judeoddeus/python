# 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
somaIdade = mediaIdade = nomehomemvelho = mulher20 = idadehomemvelho = 0
listaIdade = []
for p in range(1, 5):
    print(f'----- {p}ª Pessoa -----')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    somaIdade += idade
    # Define as mulheres menores de 20 anos
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    # Definir a idade e nome do homem mais velho
    # listaIdade.append(idade) Deixei o lista para saber que tem duas formas de fazer
    if p == 1 and sexo == 'M':
        nomehomemvelho = nome
        idadehomemvelho = idade
    if idade > idadehomemvelho:
        idadehomemvelho = idade
        nomehomemvelho = nome
# Define a média de idade do grupo
mediaIdade = somaIdade / 4
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {idadehomemvelho} anos e se chama {nomehomemvelho}')
print(f'Ao todo são {mulher20} mulheres com menos de 20 anos.')
