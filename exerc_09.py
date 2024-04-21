salario = float(input('Adicone o seu salario: '))
prest = float(input('Informe o valor da parcela do emprestimo: '))

limit_prest = salario * 0.20 

if prest > limit_prest:
    print('Infelizmnete o seu emprestimo não foi concedido!')
else: 
    print('Emprestimo concedido, Parabens!')