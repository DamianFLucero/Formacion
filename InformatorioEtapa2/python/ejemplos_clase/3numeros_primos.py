


primo = int(input("Ingrese un numero para saber si es un número primo o no: "))
contador=0


for i in range(1, primo+1):
	if primo % i == 0:
		contador = contador + 1

if contador == 2:
	print("Número primo")
else:
	print("Número no primo")