'''from random import randint
pc = randint(0, 10)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?'))

    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais, tente mais uma vez')
        else:
            print('Menos, tente mais uma vez')
print('Acertou com {} palpites'.format(palpite))'''
from random import randint
pal = randint(1, 10)
for i in range(1, 10):
    chute = int(input('Qual é o seu palpite?'))
    if chute == pal:
        print('Acertou')
    else:
        if chute < pal:
            print('Mais, tente novamente')
        else:
            print('Menos, tente novamente')