# teste de palindromo

frase = str(input('Digite uma algo para validar se é um palindromo ou não: '))
frase_limpa = frase.replace(' ','')

# fiz usando o for mas aí vi que tem como usar outro metodo

# tamanho_frase = len(frase_limpa)
# palindromo = ''
# for i in range(tamanho_frase -1, -1, -1):
#     palindromo += frase_limpa[i]

#versão melhorada: 

palindromo = frase_limpa[::-1]
print(f'a frase ao contrario ficaria: {palindromo}')
print(f'A frase que vc escrevou sem espaços fica: {frase_limpa}')
if palindromo.lower() == frase_limpa.lower():
    print(f'A frase {frase} é um palindromo.')