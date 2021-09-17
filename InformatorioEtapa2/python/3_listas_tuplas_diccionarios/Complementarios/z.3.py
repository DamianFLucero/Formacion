
'''
z.3 Simular la operación de colas de un Rapipago, que funciona con dos colas diferentes. 
El usuario llega y se ubica en la cola de menor cantidad de personas. 
Al finalizar el proceso indique cuántos elementos tiene cada cola.
'''

colaA = []
colaB = []
salida = True

print("\nIgrese nombre o 'salir' para finalizar: ")
while salida:
	ingreso = str(input(" "))
	if ingreso.lower() == 'salir':
		salida = False
	elif len(colaA) <= len(colaB):
		colaA.append(ingreso)
	else:
		colaB.append(ingreso)

print("\n#Cola A: ")
print(colaA)
print("#Cantidad de personas en cola A: ", len(colaA))
print("\n\n#Cola B: ")
print(colaB)
print("#Cantidad de personas en cola B: ", len(colaB))