print("-"*50)
print("LISTAGEM DE PREÇOS")
print("-"*50)
listagem = ("pão", 1,
            "lápis", 3,
            "borracha", 3,
            "caderno", 10)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end=" ")
    else:
        print(f"R${listagem[pos]:>7.2f}")
print("-"*50)