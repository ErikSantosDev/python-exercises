n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
#acostumar a usar o f antes das aspas e a variavel dentro das {}, código mais legivel e moderno.
if n1 == n2:
    print('Os dois números são iguais.')
elif n1 < n2:
    print(f'O número {n2} é maior')
else:
    print(f'O número {n1} é maior')