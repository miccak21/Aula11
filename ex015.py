d = int(input('Quantos dias ficou com o carro: '))
km = float(input('Quantos km percorridos: '))
td = d * 60
tkm = km * 0.15
total = td + tkm
print('O Total a pagar é de R${}'.format(total))
