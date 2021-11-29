km = int(input('Digite quantos a velocidade do seu carro: '))
cont = (km - 80) * 7
if km > 80:
    print('Você foi multado!!!')
    print('Você deverá pagar multa de: {}'.format(cont))
else:
    print('Está tudo certo, tenha um bom dia!!!')
