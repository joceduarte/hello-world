dia = float(input('Digite um dia da semana entre 1 e 7: '))

match dia:
    case 1:
        print('Dia da semana Domingo ')
    case 2:
        print('Dia da semana Segunda ')
    case 3:
        print('Dia da semana terça')
    case 4:
        print('Dia da semana Quarta')
    case 5:
        print('Dia da semana Quinta ')
    case 6: 
        print('Dia da semana Sexta')
    case 7:
        print('Dia da semana Sabado ')
    case _:
        print('Dia Invalido ') 