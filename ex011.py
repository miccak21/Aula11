l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
li = area/2
print('Sua parede tema dimensão de {} x {} e sua área é de {:.2f}m²'.format(l, a, area))
print('Para pintar sua parede, você precisara de {:.2f} litros de tinta'.format(li))
