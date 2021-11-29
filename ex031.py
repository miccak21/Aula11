p = int(input('Digite a distâcia da sua viagem em km: '))
if p > 200:
    n = p * 0.45
    print('A sua viagem foi longa então sua viagem custará: R${}'.format(n))
else:
    n = p * 0.50
    print('Você pagará R${} por sua viagem'.format(n))