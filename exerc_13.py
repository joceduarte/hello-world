nota_lab = float(input('Adicione a nota de Laboratorio: '))
nota_sem = float(input('Adicione a nota do semetre : '))
nota_final = float(input('Adicione a nota final: '))

media = (nota_lab * 2 + nota_sem * 3 + nota_final * 5) / 10

if 0 <= media < 2.9:
    resultado = 'Recuperação'
elif 3 <= media < 4.9: 
    resultado = 'Recuperação'
elif 5.0 < media: 
    resultado = 'Aprovado Parabens!'
    
print ('Resultado: ', resultado)