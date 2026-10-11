from datetime import date
ano = int(input('Digite o ano de nascimento'))
anoAtual = date.today().year
idade = anoAtual - ano
print(f'Quem nasceu em {ano} tem {idade} e terá 18 anos em {ano + 18}')
if idade == 18:
    print(f'Quem nasceu em {ano} terá 18 anos esse ano, e deverá se alistar IMEDIATAMENTE!!')
elif idade > 18:
    print(f'Quem nasceu em {ano}deveria ter se alistado em {ano + 18} e está atrasado há {idade - 18} anos')
else:
    print(f'Quem nasceu em {ano} ainda tem menos de de 18 anos, e só poderá se alista em {ano + 18}')