# 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
import math
a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
#hi = (a * a + b * b) ** (1/2)
hi = math.hypot(a,b)
print(f'A hipotenusa vai medir {hi:.2f}')
