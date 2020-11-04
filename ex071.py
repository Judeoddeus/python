# 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# R$50.00, R$20.00 R$10.00 R$1.00
print('=' * 30)
print('{:^30}'.format('BANCO NACIONAL'))
print('=' * 30)
valor_saque = int(input('Valor do saque R$'))
valor_total = valor_saque  # desse montante vou tirar o valor de saque qtas vezes puder
cedula_atual = 100
total_ced = 0
while True:
    # Verifica quantas vezes tira o valor do montante (total de  saque)
    if valor_total >= cedula_atual:
        valor_total = valor_total - cedula_atual
        total_ced += 1
    else:
        if total_ced > 0:  # Se o total for 0 ele não vai escrever
            print(f'Total de {total_ced} de R${cedula_atual:.2f}')
        if cedula_atual == 100:  # vai pegar o valor maior de cédula e se for igual vai cair o valor pra proxima cedula
            cedula_atual = 50
        elif cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_ced = 0  # cada vez que muda a nota o total de cédulas tem q voltar a zero
        if valor_total == 0:
            break
