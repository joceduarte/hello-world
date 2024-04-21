def categoria(idade): 
    if 5 <= 7: 
        return 'Infatil A'
    elif 8 <= 10:
        return 'Infantil B'
    elif 11 <= 13:
        return 'Juvenil A'
    elif 14 <= 17:
        return 'Juvenil B'
    else: 
        return 'Senior'
    
idade = int(input('Digite a Indade do atleta: '))
classificaco = categoria(idade)

print(f'O atleta esta na categoria, {classificaco}')