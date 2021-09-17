'''
Ejercicio 3: Calculadora de envío

Un minorista en línea proporciona una forma de envío urgente de $ 10.95 para el primer elemento 
y $ 2.95 para cada segundo elemento posterior. 
Escriba una función que tome el número de elementos en el pedido como su único parámetro. 
Devuelva los gastos de envío del pedido como resultado de la función. 
Incluya un programa principal que lea la cantidad de artículos comprados al usuario y muestre los gastos de envío.
'''

def elementos(cant):
	total = 0
	x = cant
	for i in range(cant):
		if i+1 == x:
			total += 10.95
			break
		else:
			total += 2.95
	print("\nElementos a enviar: ",cant)		
	print("El total del envío es: ",total)		

###


num = int(input("Ingrese cantidad de elementos a enviar: "))
elementos(num)