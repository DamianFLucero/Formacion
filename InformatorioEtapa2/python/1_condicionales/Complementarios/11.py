

nota1 = float(input("\nIngrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
	print("\nAprobado", promedio)
else:
	print("\nDesaprobado -", promedio)