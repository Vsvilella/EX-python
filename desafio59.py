from time import sleep
pri = int(input('Digite o primeiro valor: '))
seg = int(input('Digite o segundo valor: '))
op = 0
while op != 5:
    print('''
    [1] - Somar
    [2] - Multiplicar
    [3] - Dividir
    [4] - Subtrair
    [5] - Sair do Programa''')
    op = int((input('Qual é a sua opção?')))
    if op == 1:
        soma = pri + seg
        print('A soma entre {} e {} é {}'.format(pri, seg, soma))
    elif op == 2:
        print(pri * seg)
    elif op == 3:
        print(pri / seg)
    elif op == 4:
        print(pri - seg)
    elif op == 5:
        print('Finalizando...')
sleep(2)
print('Obrigado volte sempre')
print('ops')

