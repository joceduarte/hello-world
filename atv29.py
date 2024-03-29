diaria = 30.00
dias = int(input("informe quantos dias você trabalhou: "))
totaldiaria = diaria * dias 
vlrprevi = totaldiaria * 0.11
totalprevi = totaldiaria - vlrprevi
vlrir = totalprevi * 0.08
totalir = totalprevi - vlrir
print("o valor total que irá receber é: ", totalir)