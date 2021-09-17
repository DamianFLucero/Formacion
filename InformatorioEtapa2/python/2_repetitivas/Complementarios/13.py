


#13) Un grupo de 100 estudiantes presentan un exámen de Física. 
#Diseñe un diagrama que lea por cada estudiante la calificación obtenida y calcule e imprima:

#A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.
#B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
#C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.
#D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más.

A = 0
B = 0
C = 0
D = 0
E = True
print("\n\n#Programa de cálculos para examenes#\n\n")
while E == True:
	est = float(input("Ingrese nota: "))
	if est < 50:
		A += 1
	elif est < 70:
		B += 1
	elif est < 80:
		C += 1
	else:
		D += 1
	salir = int(input("\n#Para agregar otra nota presione 1, para salir 0: "))
	if salir == 0:
		E = False
	else:
		E = True
else:
	print("\n\n#Total:")
	print("Calificaciónes menor a 50:", A)
	print("Calificaciónes entre 50 y 70:", B)
	print("Calificaciónes entre 70 y 80:", C)
	print("Calificaciónes mayor a 80:", D)
	print("Cántidad de estudiantes ingresados: ", A+B+C+D)

