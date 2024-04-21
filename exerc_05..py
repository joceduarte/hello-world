num = int(input('Adicione um numero: '))

resultado = num % 2
if resultado == 0: 
    print('O numero {} é par'.format(num))
else:
    print('O numero {} é impar'.format(num))