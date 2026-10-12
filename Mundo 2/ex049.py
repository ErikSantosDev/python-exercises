# # fazer uma tabuada usando for , simpes tbm.

numero = int(input('De qual número você quer a tabuada?'))
for i in range(0, 11):
    print(f'{numero} X {i:2} = {i * numero}')