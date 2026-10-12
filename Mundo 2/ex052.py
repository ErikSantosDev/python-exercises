# programa pra identificar numero primos 

cores = {
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m',
    'limpa': '\033[0;39;49m'
}

# numero = int(input('Digite um número: '))
# primo = 0
# for i in range(1, numero):
#     if (numero % i == 0 and i != numero) and (numero % i == 0 and i != 1):
#         primo += 1
# if primo == 0 and numero != 1:
#     print('Esse numero é primo')
# else:
#     print('Esse numero Não é primo')

# abaixo, feito pelo guanabara, sendo a minha melhor na programação real, e a dele mais didatica.
numero = int(input('Digite um número: '))
total = 0
for i in range(1, numero +1):
    if numero % i == 0:
        print(f'{cores['amarelo']}{i}{cores['limpa']}')
        total += 1
    else:
        print(f'{cores['vermelho']}{i}{cores['limpa']}')
if total == 2:
    print(f'O numero {numero} foi dividido {total} vezes, e e é primo')
else:
    print(f'O numero foi dividido {total} vezes, ele não é primo')