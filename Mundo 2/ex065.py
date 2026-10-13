#  Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# minha solução:

# maior = contador = soma = n = 0
# n = int(input('Digite um número: '))
# menor = n
# soma = n
# resposta = str(input('Quer continuar [S/N/]: ').lower().strip())
# while resposta in 's':
#     n = int(input('Digite um número: '))
#     soma += n
#     contador += 1
#     if n > maior:
#         maior = n
#     if menor > n:
#         menor = n
#     resposta = str(input('Quer continuar [S/N/]: ').lower().strip())
# print(f'Você digitou {contador + 1} números, a média dos números digitados foi {soma / (contador + 1)}')

# solução melhorada:

contador = menor = maior = soma = 0
resposta = 'S'
while resposta in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    contador +=1
    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar [S/N/]: ').lower().strip())
print(f'Você digitou {contador} números, a média dos números digitados foi {soma / (contador)}, o maior número foi {maior} e o menor Número foi {menor}')