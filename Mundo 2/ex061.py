# programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. simples e facil.

primeiro_termo = int(input('Digite o primeiro termo da PA desejada: '))
razao = int(input('Digite a razão da PA desejada: '))
contador = 0
while contador < 10:
    print(primeiro_termo + razao * contador, end=' -> ')
    contador += 1
print('Fim')