

compra = float(input("\nIngrese monto de la compra: "))
azar = int(input("Ingrese número del 0 - 100: "))
descuento_menor = compra*15/100
descuento_mayor = compra*20/100
if azar < 74:
	print("\nFelicidades, obtuvo 15% de descuento sobre el total de la compra:\nImporte: ", compra - descuento_menor, "\nUsted ahorró: -", descuento_menor)
else:
	print("\nFelicidades, obtuvo 20% de descuento sobre el total de la compra:\nImporte: ", compra - descuento_mayor, "\nUsted ahorró: -", descuento_mayor)	