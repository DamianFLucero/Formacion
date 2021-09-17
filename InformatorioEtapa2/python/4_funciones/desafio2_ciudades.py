
'''
Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:

-Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
-Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.

Si ambos números son iguales, debe devolver el nombre de ambas
'''

def relacion(a,b):
	if a[1] > b[1]:
		print(a[0])
	elif a[1]< b[1]:
		print(b[0])
	else:
		print(a[0]) 
		print(b[0])		


listaA = []
listaB = []

ciudad_A = str(input("\nIngrese nombre de la primer ciudad: "))
ciudad_Ar = float(input(f"Ingrese reciclado de {ciudad_A} (en toneladas): "))
ciudad_B = str(input("Ingrese nombre de la segunda ciudad: "))
ciudad_Br = float(input(f"Ingrese reciclado de {ciudad_B} (en toneladas): "))

listaA.append(ciudad_A)
listaA.append(ciudad_Ar)
listaB.append(ciudad_B)
listaB.append(ciudad_Br)

print("\n#La ciudad que más recicló es:" )
relacion(listaA,listaB)
