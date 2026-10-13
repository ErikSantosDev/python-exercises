# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

tamanho = int(input('Quantos termos da Sequencia de Fibonacci você quer ver? '))
contador = 1
primeiro = 0
segundo = 1
total = 0
print(f'{primeiro} -> {segundo} -> ', end='')
while contador <= (tamanho - 2):
    total = primeiro + segundo
    print(total, end=' -> ')
    primeiro = segundo
    segundo = total
    contador += 1
print('Fim')