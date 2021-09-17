


#12) Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. 
#Debe diseñar un programa que permita monto por cliente y el total recaudado por la gasolinera, tomando en cuenta lo siguiente:
#• El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
#• El programa finaliza cuando se introduce una D como tipo de gasolina.

recaudado = 0
a = 50
b = 55
c = 60
d = True

while d == True:
	tipo = str(input("\n\nA- $50/L\nB- $55/L\nC- $60/L\nD- Salir\n\nOpción: "))
	if tipo.upper() == 'D':
		d = False
	else:
		nafta = float(input("Litros: "))
		if tipo.upper() == 'A':
			x = nafta*50
			print("Importe: $", x)
			recaudado+=x
		elif tipo.upper() == 'B':
			x = nafta*55
			print("Importe: $", x)
			recaudado+=x
		elif tipo.upper() == 'C':
			x = nafta*60
			print("Importe: $", x)
			recaudado+=x
		else:
			print("Opción no válida")
			continue
else:
	print("\n\n##################\nRecaudación total:\n$ ", recaudado)