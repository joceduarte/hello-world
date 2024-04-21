num_01 = float(input('Adicione um numero: '))
num_02 = float(input('Adicione segundo numero: '))

if num_01 > num_02:
    print(f'Os numeros maior: {num_01} ')
elif num_01 < num_02:
    print(f'O numero maior: {num_02}')
else: 
    print(f'Numeros iguas: {num_01 == num_02}')