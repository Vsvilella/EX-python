dados = list()
mai = men = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Peso: ")))
    r = (str(input("Quer continuar? [S/N]")))
    if r in "Nn":
        break
print(f"Ao todo você cadastrou {len(dados/2)} pessoas")
