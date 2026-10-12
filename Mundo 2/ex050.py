# fazer um programa q leia 6 numeros e mostre a soma dos numeros pares ignorando os numeros impares.
soma = 0
contador = 0
for i in range(1, 7):
    numero = int(input(f'Digite o {i}° número: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print(f'Foram somados {contador} números e a soma dos numeros pares digitados foi {soma}, os impares foram ignorasdos.')