#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

# genero = ''
# programa = 0
# while programa == 0:
#     genero = str(input('''
#     [M] Masculino
#     [F] Feminino
#     Digite seu genero: ''')).strip().lower()[0]
#     if genero == 'm' or genero == 'f':
#         programa = 1
# print(f'Genero definido para {genero}.')

# minha solução analisa a variavel programa, enquando o guanabara analisa diretamente o dado genero. sendo o dele melho, o meu só elemina a necessidade do print a mais!

# solução do guanabara a seguir:

genero = str(input('''
    [M] Masculino
    [F] Feminino
    Digite seu genero: ''')).strip().lower()[0]

while genero not in 'mf':
    genero = str(input('''
    [M] Masculino
    [F] Feminino
    Digite seu genero: ''')).strip().lower()[0]
print(f'Genero definido para {genero}.')