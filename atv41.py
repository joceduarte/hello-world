comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite a largura do terreno em metros: "))
preco_metro_tela = float(input("Digite o preço do metro de tela em reais: "))
perimetro = 2 * (comprimento + largura)
custo_tela = perimetro * preco_metro_tela
print(f"O custo para cercar o terreno com tela é de R${custo_tela:.2f}")
