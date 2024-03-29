sb = float(input("informe seu salario base: "))
gra = sb * 0.05
sg = sb + gra
imp = sb * 0.07
vlrimp = sb - imp
salario = sb + gra - imp
print(f"""o salario base acrescido da gratificação é {sg}, o salario base acrescido dos impostos é {vlrimp} 
e o salario a receber é {salario}""")