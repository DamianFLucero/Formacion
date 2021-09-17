

#c. 	Escriba un algoritmo que permita cargar una lista. 
#Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.

lista = []
bandera = True

while bandera:
	salida = int(input("\nSeleccione 1 para agregar un valor o 0 para salir: "))
	if salida == 0:
		bandera = False
	else:
		n = int(input("Ingrese un número: "))
		if n < 0:
			n = 0
			lista.append(n)
		else:
			lista.append(n)

print("Lista de números (Si ingresó numeros negativos fueron sustituidos por '0'):")
print(lista)