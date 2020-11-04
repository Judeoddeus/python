# 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tiranndo {nota1} e {nota2} a média do aluno é {media}')
if media <= 5:
    print('Aluno está REPROVADO!')
elif 5 < media < 6.9:
    print('Aluno está em RECUPERAÇÃO!')
else:
    print('Aluno está APROVADO!')
