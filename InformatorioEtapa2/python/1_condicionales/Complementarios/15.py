

horas = int(input("\nIngrese horas trabajadas: "))
complemento = 640

if horas <= 40:
	print("Importe:", horas*16)
else:
	print("Importe:", (horas-40)*20 + complemento)