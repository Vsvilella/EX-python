num = []
mai = men = 0
for c in range(0, 5):
    num.append(int(input(f"digite um valor para a posição {c}: ")))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print(f"voce digitou os valores {num}")
print(f"o maior valor foi {mai}")
print(f"o menor valor foi {men}")