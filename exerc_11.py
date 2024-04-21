import math

num_int = int(input('Adicone um numero inteiro: '))
if num_int > 0:
    num_base = 2

    loga = math.log(num_int)

    resultado_base = math.log(num_base)
    resultado = loga / resultado_base


    print("Logaritmo na base", num_base, "de", num_int, ":", resultado)
else:
    print('numero invalido')


