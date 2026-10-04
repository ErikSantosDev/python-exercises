p = str(input('Digite uma palavra: '))

print('É uma palavra em minusculo?: {}'.format(p.islower()))
print('é maiusculo?: {}'.format(p.isupper()))
print('è capitalizada?: {}'.format(p.istitle()))
print('É um numero?: {}'.format(p.isnumeric()))
print('É alfabetico?: {}'.format(p.isalpha()))
print('É alphanumerica?: {}'.format(p.isalnum()))
print('Só tem espaços?: {}'.format(p.isspace()))
print('A classe primitiva desse valor é {}'.format(type(p)))


