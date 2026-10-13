# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# minha solução: 

# n_inicial = int(input('Digite um número pra ver seu valor fatorial: '))
# n = n_inicial
# total = 1
# while n != 0:
#     total *= n
#     n -= 1
# print(f'O fatorial de {n_inicial} é {total}')

from math import factorial
n1 = int(input('Digite um numero pra saber seu valor fatorial: '))
fatorial = factorial(n1)

print(f'O fatorial de {n1} é igual a {fatorial}')