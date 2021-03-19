carro = float(input('Qual é a velocidade atual do carro? '))
if carro > 80:
    multa = (carro - 80) * 7
    print('\033[1;35mMULTADO!\033[m Você excedeu o limite de velocidade de 80km/h')
    print(f'Você deve pagar uma multa de \033[1;34mR${multa:.2f}')
print('\033[33mTenha um bom dia! Digija com segurança!')
