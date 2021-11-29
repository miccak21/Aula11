import random
esc = int(input('Escolha um numero de 0 a 5: '))
num = random.randint(0, 5)
print('O computador pensou em: ',num)
if esc == num:
    print('Você acertou!!!')
else:
    print('Tente Novamente!!!')
