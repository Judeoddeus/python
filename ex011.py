# 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2 metros quadrados.
larg = float(input('Informe a largura da parede em metros: '))
alt = float(input('Informe a altura da parede em metros: '))
area = larg * alt
tinta = area / 2
print(f'Para a área de {area:.3f}m², você vai precisar usar {tinta:.2f} litros de tinta.')
