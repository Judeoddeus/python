# 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = int(input('Informe o valor em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'''A medida em Quilômetros: {km}Km
Hectómetro: {hm}hm
Decametro: {dam}
Decimetro: {dm}
Centímetroa: {cm}cm
Milimetros: {mm}mm
''')
