casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quanto tempo você pretende pagar esse imprestimo: '))
prestacao = casa / (anos * 12)
if prestação > salario * 30 / 100:
    print('A prestação da casa seria de R$:{:.2f} e excederia os 30% do seu salario, infelizmente seu empréstimo foi negado.'.format(prestacao))
else:
    print('A prestação da sua casa seria de R${:.2f} o que seria abaixo de 30% de seu salario, então parabéns, seu emprestimo foi aprovado.'.format(prestacao))
