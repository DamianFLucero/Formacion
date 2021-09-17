

a = float(input("\nIngrese valor de lado A: "))
b = float(input("Ingrese valor de lado B: "))
c = float(input("Ingrese valor de lado C: "))

if a == b and a == c:
	print("\nTriángulo equilatero")
elif a == b or a == c or b == c:
	print("\nTriángulo isósceles")
else:
	print("\nTriángulo escaleno")