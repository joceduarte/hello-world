import math

numero = int(input('Digite um número:'))
if numero < 0:
   print('Número inválido.')
else:
   raiz = math.sqrt(numero)
   print(f'A raiz quadrada de {numero} é {raiz}')
