from datetime import date
data = int(input('Digite o ano que quer analisar. Digite 0 para analisar o ano atual '))
if data % 4 == 0 and data % 100 !=0 and data % 400 == 0:
    print('O ano de {} É bissexto'.format(data))
else:
    print('O ano de {} NAO É bissexto'.format(data))
if data == 0:
    data = date.today().year
