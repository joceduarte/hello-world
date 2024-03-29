numero = int(input("Digite um número inteiro de três dígitos (de 100 a 999): "))
if 100 <= numero <= 999:
    numeroinvertido = int(str(numero)[::-1])
    print(f"Número Gerado: {numeroinvertido}")
else:
    print("Número fora do intervalo especificado.")
