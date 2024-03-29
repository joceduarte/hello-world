hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial: "))
segundo_inicial = int(input("Digite o segundo inicial: "))
duracao_segundos = int(input("Digite a duração em segundos: "))
total_segundos_inicial = hora_inicial * 3600 + minuto_inicial * 60 + segundo_inicial
total_segundos_final = total_segundos_inicial + duracao_segundos
hora_final = total_segundos_final // 3600 % 24
minuto_final = (total_segundos_final % 3600) // 60
segundo_final = total_segundos_final % 60
print(f"O término da experiência será às {hora_final} horas, {minuto_final} minutos e {segundo_final} segundos.")
