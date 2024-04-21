num = int(input('Adicione um numero maior que zero: '))

if  num > 0: 
    num_str = str(num)
    soma = 0 
    for digito in num_str:
        soma += int(digito)
    print(f'A soma dos algoritimos é: {num}, é, {soma}')
else: 
    print('numero invalido! ')