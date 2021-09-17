'''
Ejercicio 1: Triángulos

Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros y
 devuelva la hipotenusa del triángulo, 
calculada usando el teorema de Pitágoras, como resultado de la función. 
Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, 
use su función para calcular la longitud de la hipotenusa y muestre el resultado.
'''

def hipotenusa(a,b):
	h = 0
	x = a**2 + b**2
	while h * h < x:
		h += 1
	print(h)	




print("\n\nPara calcular la hipotenusa de un triángulo: ")
catetoA = int(input("Ingrese valor de cateto A: "))
catetoB = int(input("Ingrese valor de cateto B: "))
print("\nResultado:")
hipotenusa(catetoA,catetoB)

