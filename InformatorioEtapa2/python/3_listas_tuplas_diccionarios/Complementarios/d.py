

#d. 	Realice una función que dada una lista de enteros L, y un número entero n. 
#Elimine de la lista original los elementos que sean iguales a ese número dado.


L = [1,2,3,1,2,1,2,1]
print("\n", L)
n = int(input("\nIngrese número que desee borrar de la lista: "))


for i in L:
	if n in L:
		L.remove(n)

print(L)