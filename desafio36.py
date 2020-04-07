casa = float(input('Quanto vale a casa que deseja comprar? RS '))
salario = float(input('Qual é o valor do seu salário?'))
anos = int(input('Qauntos anos deseja pagar a casa?'))
prestação = casa/(anos*12)
minimo = (30/100)*prestação
print('Para pagar a casa de {:.2f}, a sua prestação será de {:.2f} reais'.format(casa, prestação))
if prestação <= minimo:
    print('Empréstimo \033[1;32m ACEITO \033[m !!!')
else:
    print('Empréstimo \033[1;31m RECUSADO \033[m !')