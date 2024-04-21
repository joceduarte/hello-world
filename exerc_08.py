nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
    
if media < 7.0:
    print('Reprovado')
    print('Media: ', media)
elif media < 10:
    print('Aprovado')
else:
    print('A nota deve ser valida entre 0.0 e 10.0!')