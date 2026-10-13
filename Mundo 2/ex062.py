# programa que leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. simples e facil//perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da PA desejada: '))
razao = int(input('Digite a razão da PA desejada: '))
tamanho = 10
contador = 0
programa = True
mais = -1
while mais != 0: 
    while contador < tamanho:
        print(f'{primeiro_termo + razao * contador} -> ', end='')
        contador += 1
    print('Pausa')
    mais = int(input('Digite quantos numeros a mais dessa PA você quer ver:  '))
    tamanho = contador + mais
print('Fim')