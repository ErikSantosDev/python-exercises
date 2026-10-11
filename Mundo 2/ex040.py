n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota '))
media = (n1 + n2) / 2
# usei os if pra cuidar dos maiores e menores, para economizar linha usei o else pra pegar o restante, ou seja oq ficou no meio termo.
#cuidando para que n tenha ponstos segos usando o =, para que o 10 e 0 não fiquem de fora.
if media < 5 and media >= 0:
    print(f'Sua média foi {media} Infelizmente você foi REPROVADO')
elif media >= 7 and media <= 10:
    print(f'Sua média foi {media} parabéns você foi APROVADO!')
elif media >= 5 and media < 7:
    print(f'Sua média foi {media} você precisa estudar mais, ficou de recuperação!')
else:
    print(f'Sua média foi {media} e está invalida, confira as notas digitadas e tente novamente.')