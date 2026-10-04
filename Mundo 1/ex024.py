nome = str(input('Digite o nome de uma cidade: ').strip())
nomeup = nome.upper()
print('o nome da cidade começa com Santo: {}'.format(nomeup.split()[0] == 'SANTO'))
