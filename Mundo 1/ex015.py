dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('quantos KM o carro rodou? '))

print('O carro foi alugado por {:.2f} dias e rodou {:.2f} KM então o valor do aluguel a pagar será {:.2f}'.format(dias, km, (dias * 60) + (km * 0.15)))