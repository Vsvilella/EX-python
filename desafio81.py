lista = []
while True:
    lista.append(int(input("digite um valor: ")))
    r = str(input("Quer continuar? [S/N]"))
    if r in "n":
        break

print(f"Foram digitados {len(lista)} números")
lista.sort(reverse=True)
print(f"A lista de forma decrescente é {lista}")
if 5 in lista:
    print("o valor 5 faz parte da lista")
else:
    print("o valor 5 não faz parte da lista")