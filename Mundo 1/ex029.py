velocidade = int(input('Qual a velocidade do carro? '))

if velocidade < 80:
    print('Está dentro do limite de 80km/h')
else:
    print('O carro esta {} km/h a cima do limite e devera pagar R$:{:.2f} de multa'.format(velocidade - 80, 7 * (velocidade - 80)))