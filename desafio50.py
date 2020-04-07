soma = 0
cont = 0
for c in range(1, 7):
    num = (int(input('Digite um valor: ')))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você digitou {} números pares e sua soma foi {}'.format(cont, soma))