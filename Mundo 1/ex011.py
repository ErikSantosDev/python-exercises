altura = float(input('Qual a altura da parede em metros: '))
largura = float(input('Qual a largura da pardede em metros: '))
area = altura * largura

print('Sabendo que cada litro de tinta pinta 2m², e a parede tem {:.2f}m² vc precisa de {:.2f}L de tinta'.format(area, area/2))
