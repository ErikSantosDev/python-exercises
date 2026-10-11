peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em M: '))
#posso tirar a primeira condição antes do and, pq o teste anterior ja falidou essa parte, então n precisa. linha 10 de exemplo.
if peso <= 0 or altura <= 0:
    print('Informações invalidas, tente novamente')
else:
    IMC = peso / (altura * altura)
    if IMC < 18.5:
        condicao = 'Abaixo do peso'
    elif IMC < 25:
        condicao = 'Peso Ideal'
    elif IMC >= 25 and IMC < 30:
        condicao = 'Sobrepeso'
    elif IMC >= 30 and IMC < 40:
        condicao = 'Obesidade'
    else:
        condicao = 'Obesidade Mórbida'
    print(f'Você está com {peso}kg, tem {altura} de altura e sua condição é: {condicao}')