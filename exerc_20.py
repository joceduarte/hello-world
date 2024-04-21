def verificar_aposentadoria(idade, tempo):

    if idade >= 65  or tempo >= 30 or (idade >= 60 and tempo >= 25):
        return 'O trabalhador pode se aposentar! Congratuleichon'
    else: 
        return 'O trabalhador nao pode se aposentar! Todes nao deixa'

idade  = float(input('Adicone a idade do trabalhador: '))
tempo = float(input('Adicione o tempo de trabalho: '))

print(verificar_aposentadoria(idade, tempo))