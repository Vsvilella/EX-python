numero = list()
while True:
    n = int(input("digite um valor: "))
    if n not in numero:
        numero.append(n)
        print("valor adicionado")
    else:
        print("valor duplicado")
    r = str(input("Quer continuar? [S/N]"))
    if r == "Nn":
        break
print(f"você digitou {numero}")