

#b. 	Haz un programa que almacene 5 elementos en una variable del tipo lista, la modiﬁque para que cada componente sea igual al 
#cuadrado del componente original. El programa mostrara la lista resultante por pantalla.

lista = []
contador = 0


while contador < 5:
	n = int(input("Ingrese un valor: ")) 
	r = n**2
	lista.append(r)
	contador+=1
print("\n\nEl cuadrado de los numeros ingresados es:")
print(lista)