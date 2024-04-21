def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

def exibir_menu():
    print("Escolha uma operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

def realizar_operacao(operacao, a, b):
    if operacao == 1:
        return soma(a, b)
    elif operacao == 2:
        return subtracao(a, b)
    elif operacao == 3:
        return multiplicacao(a, b)
    elif operacao == 4:
        return divisao(a, b)
    else:
        return "Opção inválida."

exibir_menu()
opcao = int(input("Digite o número da operação desejada: "))

if opcao in range(1, 5):
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))

    resultado = realizar_operacao(opcao, valor1, valor2)
    print("Resultado:", resultado)
else:
    print("Opção inválida.")