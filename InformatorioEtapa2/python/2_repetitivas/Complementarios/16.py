


#16) Escribir un programa el cual lea dos valores enteros. 
#Si el primero es menor que el segundo, que imprima el mensaje ``Arriba''. 
#Si el segundo es menor que el primero, que imprima el mensaje ``Abajo''. 
#Si los números son iguales, que imprima el mensaje ``igual''. 
#Si alguno de los datos ingresados es igual a 0, que imprima un mensaje conteniendo la palabra ``Error''.

a = int(input("\n\nIngrese valor de 'A': "))
b = int(input("Ingrese valor de 'B': "))

if a == 0 or b == 0:
	print("\nError")
elif a < b:
	print("\nArriba")
elif a > b:
	print("\nAbajo")
elif a == b:
	print("\nIgual")
else:
	print("\nIngreso inválido")