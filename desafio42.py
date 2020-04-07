l1 = int(input('Digite um lado do triangulo'))
l2 = int(input('Digite outro lado do triangulo'))
l3 = int(input('Digite o ultimo lado do triangulo'))
if l1 < l2 + l3 and l2 < l1+l3 and l3 < l1+l2:
    print('Os segmentos PODEM formar um triângulo', end=' ')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    if l1 != l2 != l3 and l1 != l3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos NÃO podem formar um triângulo')