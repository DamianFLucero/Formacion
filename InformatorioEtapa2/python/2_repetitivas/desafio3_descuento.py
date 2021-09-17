
total = 0
importe = float(input("Ingrese importe de venta: "))
while importe != 0:
	print("\nDependiendo al color")
	print("1 - Rojo -40%")
	print("2 - Amarillo -25%")
	print("3 - Blanco sin descuento")
	descuento = int(input("\nSeleccione 1, 2 o 3 para aplicar el descuento correspondiente: "))
	if descuento == 1:
		final = importe*40 / 100
		print("Importe final menos 40'%' de descuento: ", importe - final)
		total = total + importe - final
	elif descuento == 2:
		final = importe*25 / 100
		print("Importe menos 25'%' de descuento: ", importe - final)
		total = total + importe - final
	else:
		final = importe
		print("Importe final sin descuento: ", importe)
		total = total + final

	importe = float(input("\nIngrese importe de venta o '0' para salir: "))
else:
	print("\n\nTotal de ventas: ", total)