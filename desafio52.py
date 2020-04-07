num = int(input('Digite um número'))
tot = 0
for i in range(1, num+1):
    if num % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(i), end=' ')
print('\n\033[m O número {} foi divisível por {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso este número é primo!')
else:
    print('E por isso este número não é primo!')