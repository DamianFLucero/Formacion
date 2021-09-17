

#e. 	Cargar m elementos en una pila, y luego copiarlos en una nueva lista.

pila = []
bandera = True



while bandera:
	pregunta = int(input("\n¿Quiere agregar un elemento a la pila?: 1-si / 2-no: "))
	if pregunta == 2:
		break
	else:
		agregar = int(input("\nIngrese el número que quiera agregar a la lista: "))
		pila.append(agregar)

elementos = pila[:]
print("", elementos)	 
