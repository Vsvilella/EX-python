from random import randint
while True:
    jogador = int(input("Digite um valor"))
    computador = randint(0, 11)
    total = jogador+computador
    tipo = str(input("Você quer par ou impar [P/I]"))
    print(f"Você jogou {jogador} e o computador {computador}. O total foi de {total}")
    if tipo == "P":
        if total % 2 == 0:
            print("você venceu")
        else:
            print("você perdeu")
            break
    elif tipo == "i":
        if total % 2 == 1:
            print("você venceu")
        else:
            print("você perdeu")
            break


