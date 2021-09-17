

libros = int(input("\nIngrese cantidad de libros: "))
total = float(input("Ingrese importe total de venta: "))
segmento = int(input("Seleccione 1/2 según:\n1-Librería\n2-Particular\nSelección: "))
if segmento == 1:
	if libros <= 24:
		print("\nImporte:", total - (total*20/100))
	else:
		print("\nImporte:", total - (total*25/100))
else:
	if libros < 6:
		print("\nImporte:", total)
	elif libros < 19:
		print("\nImporte:", total - (total*5/100))
	else:
		print("\nImporte:", total - (total*10/100)) 