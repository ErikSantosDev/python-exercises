# cores no terminal usando modo ANSI usanso \033[
# red_collor = '\033[1;31m'
# default_collor = '\033[0;39;49m'
# print('{}Erro 404{}'.format(red_collor, default_collor))

# agora usando um dicionario pra separar cores pra n precisar criar variaveis para isso:
cores = {
    'vermelho': '\033[1;31m',
    'limpa': '\033[0;39;49m'
}

print('{}Erro 404{}'.format(cores['vermelho'], cores['limpa']))