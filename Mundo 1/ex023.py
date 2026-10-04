npuro = (input('insira um numero inteiro de 0 a 9999: '))
n = npuro.zfill(4)
print('o numero digitado foi {}'.format(npuro))
print('o numero digitado contem {} digitos'.format(len(n)))
print('o numero contem {} unidades'.format(n[3]))
print('o numero contem {} dezenas'.format(n[2]))
print('o numero contem {} centenas'.format(n[1]))
print('o numero contem {} milhares'.format(n[0]))

