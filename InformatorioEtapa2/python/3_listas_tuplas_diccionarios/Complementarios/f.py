

#f. Cargar k elementos en una cola, y luego copiarlos en una nueva lista.

L = []
salir = True

while salir:
	pregunta = int(input("¿Quiere ingresar elemento a la cola?: 1-si / 2-no: "))
	if pregunta == 2:
		break
	else:
		n = input("Ingrese el elemento: ")
		L.append(n)

nueva = L[:]
print("\nLista nueva:\n", nueva)
