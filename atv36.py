numero = int(input("Digite um número inteiro de quatro dígitos (de 1000 a 9999): "))
if 1000 <= numero <= 9999:
    for digito in str(numero):
        print(digito)
else:
    print("Número fora do intervalo especificado.")
