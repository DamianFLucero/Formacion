

ventas_dia_a = float(input("\nIngrese ventas de día A: "))
ventas_dia_b = float(input("Ingrese ventas de día B: "))

if ventas_dia_a > ventas_dia_b:
	print("\nGanancia mayor en día A con:", ventas_dia_a)
elif ventas_dia_a < ventas_dia_b:
	print("\nGanancia mayor en día B con:", ventas_dia_b)
else:
	print("\nGanancias iguales en día A y B con:", ventas_dia_a)