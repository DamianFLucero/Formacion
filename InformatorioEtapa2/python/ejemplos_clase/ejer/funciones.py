def SepararSexo(p):
	edades_M = list()
	edades_F = list()
	for i in p:
		if i[1] == "M":
			edades_M.append(i[2])
		else:
			edades_F.append(i[2])

	edades = edades_F.copy()
	edades.extend(edades_M)
	return edades,edades_M,edades_F

def puntoA(personas):
	aux = list()
	for p in personas:
		aux.append(p[0])

	aux.sort()
	for i in aux:
		for p in personas:
			if p[0] == i:
				print(i, " ", p[2])

def puntoB(personas,edades):
	for p in personas:
		if p[2] == max(edades):
			print("la persona de mayor edad es: ", p[0])
		if p[2] == min(edades):
			print("la persona de menor edad es: ", p[0])

def puntoC(edades):
	promedio = 0
	for e in edades:
		promedio += e
	print("el promedio de edad es: ", promedio / len(edades))

def puntoD(edades_F,edades_M):
	promedio = 0
	for e in edades_F:
		promedio += e
	print("el promedio de edad femenino es: ", promedio / len(edades_F))

	promedio = 0
	for e in edades_M:
		promedio += e
	print("el promedio de edad masculino es: ", promedio / len(edades_M))