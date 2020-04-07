#print('{:=^40'.format('LOJA VIRTUAL'))
preço = float(input('Digite o preço das compras '))
print('''FORMAS DE PAGAMENTO
[1] - À vista/ Dinheiro/Cheque
[2] - À vista no Cartão
[3] - 2x no Cartão
[4] - 3x no Cartão ''')
opção = int(input('Qual é a opção de pagamento ?'))
if opção == 1:
    total = preço - (10 / 100 * preço)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra foi parcelada de 2x e o valor foi {:.2f} Reais'.format(total))
elif opção == 4:
    total = preço + (preço * 20/100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {:.2f}x de {:.2f} Reais'.format(totparc, parcela))
print('O valor total foi de {:.2f} Reais'.format(total))
