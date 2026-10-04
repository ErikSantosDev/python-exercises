import math
catAd = float(input('Digite o valor do cateto adjacente:'))
catOp = float(input('Digite o valor do cateto oposto:'))
hipotenusa = math.hypot(catAd,catOp)

print('o triangulo tem o cateto oposto de {:.2f}, cateto adjacente de {:.2f} e a hipotenusa de {:.2f}.'.format(catOp, catAd, hipotenusa))