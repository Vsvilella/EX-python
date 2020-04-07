from datetime import date
atual = date.today().year
nasc = int(input('Qual ano você nasceu?'))
idade = atual-nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade==18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você ainda não tem 18 anos, ainda faltam {} anos para seu alistamento'.format(saldo))
    print('Seu alistamento será em {} ano'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você ja deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {} ano'.format(ano))
