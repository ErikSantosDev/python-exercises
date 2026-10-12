#contador para contagem regressiva, exemplo usado foi o contador de 10s para ano novo.

cores = {
    'vermelho': '\033[1;31m',
    'amarelo': '\033[1;33m',
    'limpa': '\033[0;39;49m'
}

import time
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(f'{cores['amarelo']}Feliz ano noooovooooo!!{cores["limpa"]}')