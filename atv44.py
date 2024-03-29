nome = input ("informe o nome do vendedor: ")
qtd = float(input("informe a quantidade de carros vendidos: "))
vlr_total = float(input("informe o valor total de vendas: "))

vlr_carros = qtd * 50
comissao = vlr_total * 0.05 
salario = vlr_carros + comissao + 500 

print(f"o salario de {nome} ao final do mes foi: {salario} ")