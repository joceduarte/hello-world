import math

num_real = int(input('Adicone um numero : '))

if num_real > 0: 
    quadrado = num_real * num_real
    raiz = math.sqrt(num_real)
    print(f'A raiz quadrada do numero digitado é: {raiz}')
    
elif num_real <= 0:
    print('numero Invalido')