segundos = int(input("Digite um valor inteiro em segundos: "))
horas = segundos // 3600
segundosrestantes = segundos % 3600
minutos = segundosrestantes // 60
segundos_final = segundosrestantes % 60
print(f"{segundos} segundos correspondem a:")
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos_final} segundos")
