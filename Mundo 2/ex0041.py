from datetime import date
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano

# eu iria fazer desse jeito abaixo mas ficou mt repetitivo, então criarei uma variavel para a categoria e digitarei a frase uma unica vez.

# if idade >= 0 and idade <= 9:
#     print(f'Esse atleta tem {idade} e está na categoria MIRIM')
# elif idade > 9 and idade <= 14:
#     print(f'Esse atlet tem {idade} e está na categoria INFANTIL')
# elif idade > 14 and idade <= 18:
#     print(d)
if idade < 0:
    print(f'A idade inválida, verifique o ano e tente novamente.')
else:
    if idade >= 0 and idade <= 9:
        categoria = 'MIRIM'
    elif idade > 9 and idade <= 14:
        categoria = 'INFANTIL'
    elif idade > 14 and idade <= 18:
        categoria = 'JÚNIOR'
    elif idade > 18 and idade <= 25:
        categoria = 'SÊNIOR'
    elif idade > 25:
        categoria = 'MASTER'
    print(f'O atleta tem {idade} e esta na categoria {categoria}')