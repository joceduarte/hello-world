investimento_amigo1 = float(input("Digite o valor investido pelo amigo 1: "))
investimento_amigo2 = float(input("Digite o valor investido pelo amigo 2: "))
investimento_amigo3 = float(input("Digite o valor investido pelo amigo 3: "))
valor_premio = float(input("Digite o valor do prêmio: "))
total_investido = investimento_amigo1 + investimento_amigo2 + investimento_amigo3
proporcao_amigo1 = investimento_amigo1 / total_investido
proporcao_amigo2 = investimento_amigo2 / total_investido
proporcao_amigo3 = investimento_amigo3 / total_investido
premio_amigo1 = proporcao_amigo1 * valor_premio
premio_amigo2 = proporcao_amigo2 * valor_premio
premio_amigo3 = proporcao_amigo3 * valor_premio
print(f"O amigo 1 ganharia R${premio_amigo1:.2f}")
print(f"O amigo 2 ganharia R${premio_amigo2:.2f}")
print(f"O amigo 3 ganharia R${premio_amigo3:.2f}")
