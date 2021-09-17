

camisas = int(input("\nIngrese cantidad de camisas vendidas: "))
importe = float(input("Ingrese importe total de venta: "))

if camisas >= 3:
	print("Importe total con descuento:", importe - (importe*20/100))
else:
	print("\nImporte total con descuento:", importe - (importe*10/100))	