#fazer um programa q leia 5 mesos e diga qual o maior e menor peso.

for i in range(1, 6):
    peso = float(input(f'Digite o {i} peso : '))
    if i == 1:
        menor_peso = peso
        maior_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if menor_peso > peso:
        menor_peso = peso
print(f'O menor peso foi {menor_peso}')
print(f'O maior peo foi {maior_peso}')