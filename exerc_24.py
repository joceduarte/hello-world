import math


def calcular_estacionamento(chegada, partida):
    minutos_chegada = chegada[0] * 60 + chegada[1]
    minutos_partida = partida[0] * 60 + partida[1]

    diferenca_minutos = minutos_partida - minutos_chegada
    numero_horas = math.ceil(diferenca_minutos / 60)
    numero_horas = math.ceil(diferenca_minutos / 60)

    if numero_horas <= 2:
        preco = numero_horas * 1
    elif 3 <= numero_horas <= 4:
        preco = 2 + (numero_horas - 2) * 1.4
    else:
        preco = 4.8 + (numero_horas - 4) * 2

    return preco

hora_chegada = int(input("Digite a hora de chegada (0-23): "))
minuto_chegada = int(input("Digite os minutos de chegada (0-59): "))
hora_partida = int(input("Digite a hora de partida (0-23): "))
minuto_partida = int(input("Digite os minutos de partida (0-59): "))

preco_total = calcular_estacionamento((hora_chegada, minuto_chegada), (hora_partida, minuto_partida))
print(f"O preço cobrado pelo estacionamento é R${preco_total:.2f}")