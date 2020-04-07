n = s = cont = 0
while True:
    n = (int(input("digite um número para somar")))
    if n == 999:
        break
    cont += 1
    s += n
print(f"a soma dos {cont} valores é {s}!!")