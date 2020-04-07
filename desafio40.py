nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))
tot = (nota1+nota2)/2
if tot >= 7:
    print('Sua nota total foi {}. Voce está \033[31m APROVADO \033[m!!!'.format(tot))
elif 5<tot<6.9:
    print('Sua nota total foi {:.1f}. Voce está de \033[31m RECUPERAÇÃO \033[m'.format(tot))
else:
    print('Sua nota total foi {:.1f}. Você está \033[31m REPROVADO \033[m'.format(tot))