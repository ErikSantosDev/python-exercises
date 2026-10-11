r1 = int(input('Digite a primeira reta: '))
r2 = int(input('Digite a segunda reta: '))
r3 = int(input('Digite a terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 and r2 == r3:
        triangulo = 'Equilátero'
    elif r1 != r2 and r1 != r3 and r2 != r3:
        triangulo = 'Escaleno'
    else:
        triangulo = 'Isósceles'
    print(f'Essas retas formam um triangulo do tipo {triangulo}')
else:
    print('Essas retas não podem formar um triangulo')