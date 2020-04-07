peso = float(input('Digite seu peso'))
altura = float(input('Digite sua altura'))
imc = peso / (altura**2)
print('Seu IMC é {:.1f}'.format(imc))
if 18.5 > imc:
    print('Você está Abaixo do peso.')
elif 18.5 <= imc <25:
    print('Você está no Peso ideal! \033[0;31m PARBÉNS \033[m !!!' )
elif 25 <= imc < 30:
    print('Você está no Sobrepeso! \033[0;31m CUIDADO \033[m !!! ')
elif 30 <= imc < 40:
    print('Você está Obeso! \033[0;31m CUIDADO \033[m !!! ')
else:
    print('Você está em Obesidade Mórbida \033[0;31m CUIDADO \033[m !!!')