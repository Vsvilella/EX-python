numero = list()
par = list()
impar = list()
while True:
    numero.append(int(input("digite um valor: ")))
    r = str(input("Quer continuar: [S/N]"))
    if "n" in r:
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f"Os números digitados foram: {numero}")
print(f"Dentre eles, são pares: {par}")
print(f"E impares: {impar}")