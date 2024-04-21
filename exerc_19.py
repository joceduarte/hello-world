def tipo_de_triangulo(a, b, c):

    if  a >= b+c or b >= a+c or c>= a+b:
        return 'Nao e um triangulo'

    if a == b == c:
        return 'Trinagulo equilatero'
    elif a == b or a == b or b == c:
        return 'Triangulo isósceles'
    else: 
        return 'Triangulo escaleno'

valor_a = float(input('Digite o valor de A: '))
valor_b = float(input('Digite o valor de B:'))
valor_c = float(input('Digite o valor de C: '))
print(tipo_de_triangulo(valor_a, valor_b, valor_c))