salario = float(input('Quao seu salario: '))
# if salario > 1250:
#     print('Seu salario reajustado ficará R${:.2f}'.format(salario + (salario * 10 / 100)))
# else:
#     print('Seu salario reajustado ficará R${:.2f}'.format(salario + (salario * 15 / 100)))
# a seguir a forma mais profissional, deixando a logica no if e else, enquanto a resposta se consentra no final.
if salario > 1250:
    reajuste = salario + (salario * 10 / 100)
else:
    reajuste = salario + (salario * 15 / 100)
print('Seu salario reajustado ficaria {:.2f}'.format(reajuste))