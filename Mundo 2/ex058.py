# um programa onde o  computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
palpite = int(input('Tente adivinhar um numero de 0 a 10: '))
tentativas = 1
while palpite != computador:
    tentativas += 1
    if palpite < computador:
        palpite = int(input('Errou, tente novamente. Dica: É um numero maior'))
    else:
        palpite = int(input('Errou, tente novamente. Dica: É um numero menor'))
print(f'Parabens você acertou na {tentativas}° tentativa, o número escolhido pelo computador era {computador}!')