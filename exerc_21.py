def ano_bissexto(ano):

    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False

ano = int(input('Digite o ano: '))

if ano_bissexto(ano):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano}, nao e bissexto')