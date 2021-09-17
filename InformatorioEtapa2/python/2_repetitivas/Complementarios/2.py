

#2) Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.

n = int(input("\n\nIngrese uel valor de 'n': "))
x = 0


for i in range (1,n+1):
	r = i**2
	x = x + r
else:
	print("\nLa suma de los cuadrados de 1 a 'n' es:", x)
