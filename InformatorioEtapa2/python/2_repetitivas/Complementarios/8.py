

#8) Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
#El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.


salida = True
total = 0

while salida == True:
	cantidad = int(input("Cantidad de producto: "))
	precio = float(input("Precio unitario del producto: "))
	x = precio*cantidad
	total+=x
	salida = int(input("\n-Presione 1 para agregar otro producto, 0 para salir: "))
	if salida == 0:
		salida = False
	else:
		salida = True
else:
	print("\n######\nTotal:", total,"\n######")