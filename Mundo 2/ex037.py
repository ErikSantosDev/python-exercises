numero = int(input('Digite o numero para converter: '))
option = int(input('[1]Binario\n[2]Octal\n[3]Exadecimal\nQual opção vc deseja ver? '))
#o [2:] é pra ignorar os primeiros 2 digitos, q são a identificação, no caso pega no digito posição 2, q seria o terceiro em diante.
if option == 1:
    print('O número {} em bínario seria {}'.format(numero, bin(numero)[2:]))
elif option == 2:
    print('O número {} em Octal seria {}'.format(numero, oct(numero)[2:]))
elif option == 3:
    print('O número {} em Hexadecimal seria {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida, tente novamente!')