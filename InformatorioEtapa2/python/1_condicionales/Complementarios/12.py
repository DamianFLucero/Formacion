

articulo = str(input("Ingrese nombre del artículo: "))
precio = float(input("Ingrese precio del artículo: "))
clave = str(input("\n-Seleccione clave '01' para acceder al 10% de descuento\n-Seleccione clave '02' para acceder al 20% de descuento\nOpción: "))

if clave == '01':
	print("\nNombre: ", articulo, "\nClave:  ", clave, "\nPrecio: ", precio, "\nPrecio c/descuento: ", precio - precio*10/100)
elif clave == '02':
	print("\nNombre: ", articulo, "\nClave:  ", clave, "\nPrecio: ", precio, "\nPrecio c/descuento: ", precio - precio*20/100)
else:
	print("\nClave incorrecta")	