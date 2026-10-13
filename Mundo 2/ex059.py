# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
programa  = True
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

while programa == True:
    option = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    >>>>>>>> Digite a opção desejada: '''))
    if option == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif option == 2:
        print(f'{n1} X {n2} = {n1 * n2}')
    elif option == 3:
        if n1 > n2:
            print(f'O maior numero entre {n1} e {n2} é {n1}')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}')
        else:
            print('Os números são iguais')
    elif option == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif option == 5:
        programa = False
print('Finalizando o programa....')
sleep(3)
print('Programa finalizado, volte sempre!!')