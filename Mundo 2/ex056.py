# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# eu uso IA para validar o funcionamento do codigo, como uso o gemini pq geralmente só faço pesquisas ou preciso validar codigos simples, mas dessa vez ele estava indicando erro de logica, mas ai testei e está funcionando perfeitamente kkkk. 

idade_total = 0
idade_homem = 0
mulheres = 0
nome_homem = ''
homem_velho = ''
idade = 0
for i in range(1, 5):
    idade = int(input(f'Digite a idade da {i}° pessoa: '))
    genero = int(input('''E qual o genero dela? 
    [0] Homem
    [1] Mulher'''))
    idade_total += idade
    if genero == 0:
        nome_homem = str(input('Digite o nome do homem: '))
    if genero == 1 and idade < 20:
        mulheres +=1
    if genero == 0 and idade > idade_homem:
        homem_velho = nome_homem
        idade_homem = idade
print(f'A media de idade das pessoas lidas é {idade_total / 4}')
print(f'A quantidade de mulheres com menos de 20 anos é {mulheres}')
print(f'O Homem mais velho é o {homem_velho}')
