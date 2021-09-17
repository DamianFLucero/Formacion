


#14) Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. 
#Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras, tales como pepinillos, champiñones o cebollas. 
#Desarrolle una solución que calcule el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras. 
#El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño, más el número de ingredientes. 
#En particular el costo total se calcula sumando:

#- un costo fijo de preparación.
#- un costo variable que es proporcional al tamaño de la pizza.
#- un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo)

pequeña = 90
mediana = 130
grande = 200
costo = 100
ing = 20
a = ""
b = ""
c = ""

tamaño = int(input("\nIngrese tamaño de la pizza:\n1- Pequeña\n2- Mediana\n3- Grande\nSeleccione: "))
ingr = int(input("\nIngrese 1,2 o 3 dependiendo de cuántos ingredientes quiere agregar a la pizza entre pepinillos, champiñones o cebolla: "))

for i in range(ingr):
	if i == 1:
		comb = str(input("Ingrese ingrediente: "))
		a = comb
	elif i == 2:
		comb = str(input("Ingrese ingrediente: "))
		b = comb
	else:
		comb = str(input("Ingrese ingrediente: "))
		c = comb	

if tamaño == 1:
	print("\n\n\n#Pedido:\n- Pizza pequeña\n- Salsa y carne\n-", a, b, c, "\n\n#Importe Total: $", (pequeña + costo + (ingr*ing)) * 1.5)
elif tamaño == 2:
	print("\n\n\n#Pedido:\n- Pizza mediana\n- Salsa y carne\n-", a, b, c, "\n\n#Importe Total: $", (mediana + costo + (ingr*ing)) * 1.5)
elif tamaño == 3:
	print("\n\n\n#Pedido:\n- Pizza grande\n- Salsa y carne\n-", a, b, c, "\n\n#Importe Total: $", (grande + costo + (ingr*ing)) * 1.5)
