from random import randint
option = int(input('''Vamos jogar pedra papel e tesoura
[0] Pedra
[1] Papel
[2] Tesoura

Escolha uma opção: '''))
options = ['pedra', 'papel', 'tesoura']
optionComputador = randint(0,2)
computador = options[optionComputador]
if option < 0 or option > 2:
    print('Opção invalida, tente novamente')
else:
    if option == optionComputador:
        print(f'O computador também escolheu {computador} o jogo EMPATOU!')
    elif (option == 0 and optionComputador == 1) or (option == 1 and optionComputador == 2) or (option == 2 and optionComputador == 0):
        print(f'O computador escolheu {computador} você PERDEU')
    else:
        print(f'O computador escolheu {computador} você GANHOU')
