
'''
cargar una lista con el nonbre, sexo y edad de todo el curso

a) mostrar la lista de asistencia ordenada por nombre
b) mostrar el nombre del alumno de mayor y menor edad
c) mostrar el promedio de edad del curso
d) mostrar el promediode edad del sexo femenino y masculino
'''
from funciones import *

personas = [['juan','M',19],['pedro','M',25],['maria','F',18],['marcos','M',32],['carla','f',25],
			['noelia','f',21],['carlos','M',42],['sofia','F',42],['nicolas','M',29],['alejandro','M',22]]

edad_general,edadM,edadF = SepararSexo(personas)

while True:
	op = input(("a) mostrar la lista de asistencia ordenada por nombre\n  b) mostrar el nombre del alumno de mayor y menor edad\nc) mostrar el promedio de edad del curso\nd) mostrar el promediode edad del sexo femenino y masculino\n"))
	if op == 'a':
		puntoA(personas)
		print(" ")
	elif op == 'b':
		puntoB(personas,edad_general)
		print(" ")
	elif op == 'c':
		puntoC(edad_general)
		print(" ")
	elif op == 'd':
		puntoD(edadF,edadM)
		print(" ")
	else:
		break
	print("#######################################################")
