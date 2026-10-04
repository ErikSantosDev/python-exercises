metros = float(input('Digite a quantidade de metros: '))
cm = metros * 100
mm = metros * 1000
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000
print('{} metros é igual a {:.1f} decímetros'.format(metros, dm))
print('{} metros é igual a {:.1f} centímetros'.format(metros, cm))
print('{} metros é igual a {:.1f} milímetros'.format(metros, mm))
print('{} metros é igual a {:.1f} decâmentros'.format(metros, dam))
print('{} metros ´igual a {:.1f} hectômetros'.format(metros, hm))
print('{} metros é igual a {:.1f} kilometros'.format(metros, km))
