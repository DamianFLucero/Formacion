

print("\nPara saber si un numero 'n' es divisor de un número 'm':")
n = float(input("Ingrese valor de 'n': "))
m = float(input("Ingrese valor de 'm': "))
if m % n == 0:
	print("El número 'n' (", n,") es divisor de 'm' (", m,")")
else:
	print("El número 'n' (", n,") no es divisor de 'm' (", m,")")