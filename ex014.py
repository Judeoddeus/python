#  014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Informe a temperatura em °C: '))
fah = (celsius * 1.8) + 32
print(f'A temperatura de {celsius} ºC corresponde a {fah} ºF!')
