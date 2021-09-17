


grupo1 = 0 #-100 colillas
grupo2 = 0 #entre 99/200 colillas
grupo3 = 0 #200 colillas en adelante
contador = 0

personas = int(input("\nCantidad de registros a ingresar: "))
while contador < personas:
	contador = contador + 1 
	colillas = int(input("\nIngrese cantidad de colillas recolectadas: "))
	if colillas < 100:
		grupo1 = grupo1 + 1
		print("Grupo 1")
	elif colillas >= 100 and colillas < 200:
		grupo2 = grupo2 + 1
		print("Grupo 2")
	else:
		grupo3 = grupo3 + 1
		print("Grupo 3")
else:
	est1 = grupo1*100 / personas
	est2 = grupo2*100 / personas
	est3 = grupo3*100 / personas
	print("\n\nPorcentajes de recolección:\nGrupo 1 (menos de 100 colillas):", est1,"%\nGrupo 2 (de 100 a 199 colillas):", est2, "%\nGrupo 3 (de 200 colillas en adelante):", est3, "%")