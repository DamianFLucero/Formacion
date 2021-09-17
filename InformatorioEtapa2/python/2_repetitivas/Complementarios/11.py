

#11) Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.

print("\nPara conocer los divisores de 'n'")
n = int(input("Ingrese 'n': "))
print("")
for i in range(1,n+1):
	if n%i == 0:
		print(i, ",", end="")
else:
	print("Fin")
