


contador = 0
grande = 0
print("\nIngrese 10 numeros:\n")
while contador < 10:
	numero = int(input("Ingrese número: "))
	contador += 1
	while numero > grande:
		grande = numero
else:
	print("\nNúmero grande:", grande)