


#6) Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero.

n1 = int(input("\n\nIngrese 'n1': "))
n2 = int(input("Ingrese 'n2': "))
print("")
suma = 0

if n1 > n2:
	print("Error, 'n1' > 'n2'.\nVuelva a intentarlo.")
else:
	for i in range(n1,n2+1):
		if i % 2 == 0:
			print(i)
			suma+=i
	print("\n#La suma de los multiplos de 2 entre 'n1' y 'n2' es: ", suma)



