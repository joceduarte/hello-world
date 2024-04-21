def calcular_preco_final(valor, estado):

    if estado == 'MG':
        imposto = 0.07
    elif estado == 'SP':
        imposto = 0.12
    elif estado == 'RJ':
        imposto = 0.15
    elif estado == 'MS':
        imposto = 0.08
    else:
        return 'Estado nao valido'
    
    valor_final = valor * (1 + imposto)
    return f"O preço final do produto para o estado {estado} é R${valor_final:.2f}"


produto = float(input('Adicione o valor do produto: '))
estado = input('Adicione o estado de destino (MG, SP, RJ, MS): ').upper()

print(calcular_preco_final(produto, estado))