# 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
print('{:=^40}'.format(' LOJAS HINOMOTO '))
valor = float(input('Valor da compra R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual a sua opção? '))
if opcao == 1:
    valorFinal = valor - (valor * 0.1)
elif opcao == 2:
    valorFinal = valor - (valor * 0.05)
elif opcao == 3:
    valorFinal = valor
    print(f'Sua compra será parcelada em 2x de R${valorFinal/2:.2f} SEM JUROS. ')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    valorParcela = (valor + (valor * 0.2)) / parcelas
    valorFinal = valor + (valor * 0.2)
    print(f'Sua compra será parcelada em {parcelas}x de R${valorParcela:.2f} COM JUROS. ')
else:
    valorFinal = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(f'Sua compra de R${valor:.2f} vai custar R${valorFinal:.2f} no final.')
