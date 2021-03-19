# 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.
import math

angulo = int(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {angulo:.2f} tem o SENO de {math.sin(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo:.2f} tem o COSSENO de {math.cos(math.radians(angulo)):.2f}')
print(f'O ângulo de {angulo:.2f} tem a TANGENTE {math.tan(math.radians(angulo)):.2f}')
