base_1 = float(input('Adicone o valor da base maior: '))
base_2 = float(input('Adicione o valor da base Menor: '))
altura = float (input('Adicione o valor da altura: ' ))
a = 2 

area = ((base_1 + base_2) * altura) / a

if base_1 > 0 and base_2 > 0 and altura > 0:
    print('A area do trapézio é: ', area)
else:
    print('Valores precisam ser maior que zero!')





