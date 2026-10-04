ano = (int(input('Digite o ano que deseja saber se é bissexto: ')))
# ano % 4 == 0 and ano % 100 != 0 pega todos os numeros divisiveis por 4, ignorando os que terminam com 00, pq 100 != 0, o ano % 400 == 0 pega só os q terminam com 00
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))