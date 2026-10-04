km = float(input('De quantos KM é sua viagem? '))
if km <= 200:
    print('O valor da passagem é R${}'.format(km * 0.5))
else:
    print('Como você vai viajar mais que 200km o valor da passagem é R${}'.format(km * 0.45))