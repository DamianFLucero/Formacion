


#15) En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un número que se escoge
# al azar. Si el número escogido es menor que 50 el descuento es del 15% sobre el total de la compra,
# si es mayor o igual a 50 el descuento es del 20%. Obtener cuánto dinero se le descuenta.

total = float(input("\nIngrese total de la compra: "))
print("\nSeleccione un número de 0 a 100 para obtener un descuento del 15% o 20% sobre el total de la compra.")
n = int(input("Ingrese número: "))

if n < 50:
	x = total - (total*15/100)
	print("\n\n# ¡Felicidades! Premio del 15% de descuento sobre el total de la compra.\nTotal a pagar: $", x)
elif n >= 50:
	x = total - (total*20/100)
	print("\n\n# ¡Felicidades! Premio del 20% de descuento sobre el total de la compra.\nTotal a pagar: $", x)
else:
	print(total)