lista = [[], []]
valor = 0
for i in range(1,8):
    valor = (int(input("digite um número: ")))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f"Os valores pares são: {sorted(lista[0])}")
print(f"Os valores impares são: {sorted(lista[1])}")

