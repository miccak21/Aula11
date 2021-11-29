from math import sqrt
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento  do cateto adjacente: '))
h = (c1 * c1) + (c2 * c2)
raiz = sqrt(h)
print('A hipotenusa vai medir {:.2f}'.format(raiz))
