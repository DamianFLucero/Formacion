print("Para determinar tipo de triángulo ingrese:")
a = float(input("\nIngrese lado A del triángulo (lado más lárgo): "))
b = float(input("\nIngrese lado B del triángulo: "))
c = float(input("\nIngrese lado C del triángulo: "))

if a >= b + c:
	print("No es un triángulo")
elif a ** 2 == b ** 2 + c ** 2:
	print("Triángulo rectángulo")
elif a ** 2 > b ** 2 + c ** 2:
	print("Triángulo obtusángulo")
elif a **2 < b ** 2 + c ** 2:
	print("Triángulo acutángulo")
else:
	("Error")