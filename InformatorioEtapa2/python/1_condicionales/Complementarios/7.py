

compra = float(input("\nIngrese monto de la compra: "))
if compra < 1000:
	print("\nTotal: ", compra)
else:
	descuento = compra - (compra*15 / 100)
	print("\nDescuento 15%\nTotal: ", descuento) 