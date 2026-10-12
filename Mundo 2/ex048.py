# mostrar a soma de todos os numeros impares que são multiplos de 3 de 1 a 500. Simples também.
#fiz usando um if i % 3 == 0, mas percebi q n precisa, afinal o range pode pegar os multiplos de 3 impares apenas, q seriam a cada 6 numeros. por isso 3, 501, 6.
soma = 0
contador = 0
for i in range(3, 501, 6):
    soma += i
    contador += 1
print(f'O resultado das somas dos numeros impares que são multiplos de 3 de 1 a 500 é {soma} e foram somados um total de {contador} números.')