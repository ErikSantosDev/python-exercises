from random import randint

numero = randint(0, 5)
#pra ter certeza que o código funciona use a linha abaixo para mostrar o numero sorteado antes de dar a resposta.
#print('O número é {}'.format(numero))
n = int(input('Tente adivinhar o número entre 0 e 5: '))

if n == numero:
    print('Parabéns vc acertou, o número escolhido realmente era {}'.format(n))
else:
    print('Infelizmente vc errou, o número escolhido era {}'.format(numero))