

salir = 1

while salir > 0:
	print("\nPara averiguar el perímetro de un triángulo:")
	a = float(input("Ingrese lado A del triángulo: "))
	b = float(input("Ingrese lado B del triángulo: "))
	c = float(input("Ingrese lado C del triángulo: "))
	print("\nEl perímetro del triángulo es: ", a+b+c)
	salir = int(input("\nPara averiguar el perímetro de otro triángulo ingrese '1'; ingrese '0' para salir: "))
else:
	print("\n###\nFin\n###")