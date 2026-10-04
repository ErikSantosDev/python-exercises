n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo numero '))
n3 = int(input('Digite o terceiro numero '))

#usar o >= inves do > apenas, tira o bug de numeros iguais, pq se o n1 e o n2 for igual, vai dizer q o n3 é o maior, independente da realidade.
if n1 >= n2 and n1 >= n3:
    print('O numero {} é o maior'.format(n1))
elif n2 >= n1 and n2 >= n3:
    print('O numero {} é o maior'.format(n2))
else:
    print('O numero {} é o maior'.format(n3))

if n1 <= n2 and n1 <= n3:
    print('O numero {} é o menor'.format(n1))
elif n2 <= n1 and n2 <= n3:
    print('O numero {} é o menor'.format(n2))
else:
    print('O numero {} é o menor'.format(n3))