

#g. 	Cargar dos listas con la misma cantidad de elementos. Luego mezclarlas, cargándolas ordenadas en otra lista.

pares = []
impares = []
salir = True

while salir:
	pregunta = int(input("\nPara agregar número impar presione 1, para agregar número par presione 2, para salir presione 3: "))
	if pregunta == 1:
		n = int(input("Ingrese número impar: "))
		impares.append(n)
	elif pregunta == 2:
		n = int(input("Ingrese número par: "))
		pares.append(n)
	elif pregunta == 3:
		break
	else:
		continue


lista = pares+impares
lista.sort()
print(lista)
