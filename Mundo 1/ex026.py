from unicodedata import normalize
nome = input('Digite o nome Completo: '.strip())
nomeup = nome.upper()
nnormal = normalize('NFKD', nomeup).encode('ASCII', 'ignore').decode('ASCII')
print('Seu nome contem {} vezes a letra A'.format(nnormal.count('A')))
print('A primeira leta A aparece na posição {}'.format(nnormal.find('A')))
print('A ultima letra A aparece na posição {}'.format(nnormal.rfind('A')))