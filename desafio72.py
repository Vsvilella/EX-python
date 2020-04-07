cont = ("zero", "um", "tres", "quatro", "cinco",
        "seis", "sete", "oito", "nove", "dez")
while True:
    num = int(input("digite um número de 0 a 10"))
    if 0 <= num <= 10:
        break
    print("tente novamente.", end=" ")
print(f"você digitou o número {cont[num]}")