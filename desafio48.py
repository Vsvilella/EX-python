soma = 0
cont = 0
for im in range(1, 501, 2):
    if im % 3 == 0:
        cont = cont+1
        soma = soma+im
print('A soma de todos os {} valores é {}'.format(cont, soma))