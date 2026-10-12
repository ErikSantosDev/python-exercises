# programa que leia 7 idades e diga quantas são maiores ou menores de idade.
from datetime import date
maioridade = 0
menoridade = 0
ano_atual = date.today().year
for i in range(1, 8):
    ano = int(input(f'Digite a {i}° data de nascimento: '))
    if ano_atual - ano < 21:
        menoridade += 1
    else:
        maioridade += 1
print(f'Dos anos digitados tivemos {maioridade} maior de idade e {menoridade} menores de idade')