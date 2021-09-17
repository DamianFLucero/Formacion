

tamaño = int(input("\nSeleccione un número según tamaño del pez:\n\n(1) Tamaño normal\n(2) Tamaño por debajo de lo normal\n(3) Tamaño un poco por encima de lo normal\n(4) Tamaño sobredimensionado\n\nOpción: "))

print("\n")
if tamaño == 1:
	print("Pez en buenas condiciones")
elif tamaño == 2:
	print("Pez con problemas de nutrición")
elif tamaño == 3:
	print("Pez con síntomas de organismo contaminado")
elif tamaño == 4:
	print("Pez contaminado")
else:
	print("Vuelva a intentarlo")