import math


def calcular_media (nota1, nota2):
    peso1 = 1 
    peso2 = 2 

    media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    return media_ponderada

def verificar_aprovado(media_ponderada):
    if media_ponderada >= 70:
        return('Aprovado')
    else:
        return('Reprovado')
    
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = calcular_media(nota1, nota2)

resultado = verificar_aprovado(media)

print('Media do aluno:', media)
print('Resultado: ', resultado)
