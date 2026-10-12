# Fazer um sistema que mostre 10 termos de uma PA, lendo o numero inicial, e a razão dessa PA. Simples também.

numero_inicial = int(input('Digite o número inicial pra fazer a PA: '))
razao = int(input('Digite o número da razão da sua PA: '))

for i in range(0, 10,):
    print(f'{numero_inicial + i * razao}', end=' -> ')