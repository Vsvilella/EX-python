n = (int((input("digite um valor: "))), int((input("digite um valor: "))), int((input("digite um valor: "))), int((input("digite um valor: "))))
print(f"os valores digitados foram: {n}")
print(f"o número 9 foi digitado {n.count(9)} vezes")
if 3 in n:
    print(f"O núumero 3 está na {n.index(3)} posição")
else:
    print("O valor 3 não foi encontrado")
print(f"os valores pares foram ")
for i in n:
    if i % 2 == 0:
        print(i, end=" ")
