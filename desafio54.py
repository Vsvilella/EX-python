from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range (1, 4):
    ano = int(input('Em que ano a {} pessoa nasceu?'.format(i)))
    if ano <= atual - 18:
        print('Esta pessoa é maior de idade')
        totmaior += 1
    else:
        print('Esta pessoa é menor de idade')
        totmenor += 1
print('Ao todo tivemos {} maiores de idade e {} menores de idade'.format(totmaior, totmenor))