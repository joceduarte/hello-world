mes = int(input('Adicione um numero para saber o mês correspondente: '))

match mes:
    case 1:
        print('Corresponde ao mes Janeiro')
    case 2:
        print('Corresponde ao mes de Fevereiro')
    case 3:
        print('Corresponde ao mes de Março')
    case 4:
        print('Corresponde ao mes de Abril ')
    case 5:
        print('Corresponde ao mes de Maio ')
    case 6:
        print('Corresponde ao mes de Junho ')
    case 7:
        print('Corresponde ao mes de Julho')
    case 8:
        print('Corresponde ao mes de Agosto ')
    case 9:
        print('Corresponde ao mes de Setembro')
    case 10:
        print('Corresponde ao mes de Outubro ')
    case 11:
        print('Corresponde ao mes de Novembro')
    case 12:
        print('Corresponde ao mes de Dezembro ')
    case _:
        print('Numero não corresponde aos meses do  Mes!!!')