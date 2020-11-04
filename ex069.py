# 69: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
maior18 = mulhermenor20 = homens = 0
while True:
    print('-'*30)
    print('     CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]

    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1

    continuar = ''
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior18} ')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulhermenor20} mulheres com menos de 20 anos.')

