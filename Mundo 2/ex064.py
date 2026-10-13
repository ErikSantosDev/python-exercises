# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = total = 0
contador = -1
while n != 999:  
    total += n
    programa = n
    contador += 1
    n = int(input('Digite um número, sendo 999 a condição de parar: '))
print(f'Você digitou {contador} números, e a soma deles é {total}')