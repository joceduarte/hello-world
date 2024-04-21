

def verifica_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return f"O número {numero} é divisível por 3 e por 5 simultaneamente."
    elif numero % 3 == 0:
        return f"O número {numero} é divisível por 3, mas não por 5."
    elif numero % 5 == 0:
        return f"O número {numero} é divisível por 5, mas não por 3."
    else:
        return f"O número {numero} não é divisível por 3 nem por 5."

numero = int(input("Digite um número inteiro: "))

print(verifica_divisibilidade(numero))

