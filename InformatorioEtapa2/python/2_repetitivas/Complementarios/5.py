
n = int(input("\nPara determinar si un numero es par o impar, ingrese un número: "))

while n > 0:
	if n % 2 == 0:
		print("\nNúmero par")
	else:
		print("\nNúmero impar")
	n = int(input("\nPara determinar si un numero es par o impar, ingrese un número o 0 para salir: "))
else:
	print("\nFin")