

print("Encuesta sobra contaminación")

contaminacion = []

salida = True


while salida == True:
	nivel = (int(input("Ingrese un valor del 1 al 10 respecto a cuanto conoce sobre la contaminación: ")))
	if (nivel <= 10) and (nivel >= 1): 
		contaminacion.append(nivel)
	else:
		print("Valor incorrecto")
		continue
	valor = input("¿Desea agregar otro valor? Si/No: ")
	if valor.lower() == 'si':
		salida = True
	else:
		salida = False
else:
	contaminacion.sort()
	print(contaminacion)