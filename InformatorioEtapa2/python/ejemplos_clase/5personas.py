
'''
cargar una lista con el nonbre, sexo y edad de todo el curso

a) mostrar la lista de asistencia ordenada por nombre
b) mostrar el nombre del alumno de mayor y menor edad
c) mostrar el promedio de edad del curso
d) mostrar el promediode edad del sexo femenino y masculino
personas = list()
seguir = input("quiere cargar una alumno? SI o NO: ")
while seguir.lower() == "si":
	nombre = input("ingrese el nombre del alumno: ")
	sexo = input("ingrese M o F: ")
	edad = int(input("ingrese su edad: "))
	alumno = [nombre,sexo,edad]
	personas.append(alumno)
	seguir = input("desea seguir cargando alumnos?: SI o NO: ")
'''

personas = [['juan','M',19],['pedro','M',25],['maria','F',18],['marcos','M',32],['carla','f',25],
			['noelia','f',21],['carlos','M',42],['sofia','F',42],['nicolas','M',29],['alejandro','M',22]]

#a)
aux = list()
for p in personas:
	aux.append(p[0])

aux.sort()
for i in aux:
	for p in personas:
		if p[0] == i:
			print(i, " ", p[2])


#b)
edades_M = list()
edades_F = list()
for i in personas:
	if i[1] == "M":
		edades_M.append(i[2])
	else:
		edades_F.append(i[2])

edades = edades_F.copy()
edades.extend(edades_M)

for p in personas:
	if p[2] == max(edades):
		print("la persona de mayor edad es: ", p[0])
	if p[2] == min(edades):
		print("la persona de menor edad es: ", p[0])

#c)
promedio = 0
for e in edades:
	promedio += e
print("el promedio de edad es: ", promedio / len(edades))

#d)
promedio = 0
for e in edades_F:
	promedio += e
print("el promedio de edad femenino es: ", promedio / len(edades_F))

promedio = 0
for e in edades_M:
	promedio += e
print("el promedio de edad masculino es: ", promedio / len(edades_M))


