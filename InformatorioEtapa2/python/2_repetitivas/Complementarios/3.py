


contador = 0
total = 0

print("\nPara conocer el producto entre A y B ingrese:")
a = int(input("Ingrese número A: "))
b = int(input("Ingrese número B: "))

while contador < b:
	total += a
	contador += 1
else:
	print("\nResultado: ", total)