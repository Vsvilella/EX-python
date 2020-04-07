from math import factorial
num = int(input('Digite um número para calcular seu fatorial'))
fat = factorial(num)
print('Calculando o fatorial de {}: {}'.format(num, fat))

fatorial = 1
lista = []
for i in range(1, num+1):
    fatorial *= i
    lista.append(i)
    print(lista)

print(fatorial)