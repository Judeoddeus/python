# 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input('Valor da casa R$'))
salario = float(input('Salário do comprador R$'))
anos = int(input('Quantos anos de financiamento: '))
prestação = valorCasa / (anos * 12)
minimo = salario * 0.3
print(f'Para pagar uma casa de R${valorCasa:.2f} em {anos} anos a prestação será de R${prestação:.2f}')
if prestação <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
