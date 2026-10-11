valor = float(input('Digite o valor da compra: R$:'))
formaPagamento = int(input('''Digite a forma de pagamento:
[ 1 ] À vista em dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Até 2X no cartão
[ 4 ] 3X ou mais no cartão'''))

if formaPagamento < 1 or formaPagamento > 4:
    print('Forma de pagamento Invalida, tente novamente')
else:
    if formaPagamento == 1:
        ValorFinal = valor - (valor * 10) / 100
    elif formaPagamento == 2:
        ValorFinal = valor - (valor * 5) / 100
    elif formaPagamento == 3:
        ValorFinal = valor
        ValorParcela = valor / 2
        print(f'Você pagara 2 vezes de R$:{ValorParcela:.2f}')
    else:
        parcelas = int(input('Em quantas parcelas você quer pagar?'))
        ValorFinal = valor + (valor * 20)/ 100
        ValorParcela = ValorFinal / parcelas
        print(f'Você deverá pagar {parcelas} vezes de {ValorParcela:.2f}')
    print(f'O valor total a pagar será de {ValorFinal:.2f}')