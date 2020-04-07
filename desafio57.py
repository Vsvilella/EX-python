s = str(input('Digite o seu sexo [M/S]: ')).upper()
while s not in 'SM':
    s = str(input('Sexo inválido, Digite o seu sexo [M/S]:'))
print('Sexo {} registrado com sucesso'.format(s))