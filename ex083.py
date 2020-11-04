expressao = str(input('Digite a expressão: '))
abre = []
fecha = []
for simbolo in expressao:
    if simbolo == '(':
        abre.append('(')
    elif simbolo == ')':
        fecha.append(')')
if len(abre) == len(fecha):
    print('Expressão correta.')
else:
    print('Expressão errada.')
