

#9) Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. 
#Desea obtener de todas las personas que alcance a encuestar en un día, que porcentaje tiene estudios de primaria, 
#secundaria, carrera técnica, estudios profesionales y estudios de posgrado.

primaria = 0
secundaria = 0
tecnicatura = 0
profesional = 0
posgrado = 0
persona = 0
salir = True

while salir:
	print("\n\nCenso nacional de población y vivienda")
	persona += 1
	n = int(input("¿Posee estudios primarios?: 1-si / 2-no: "))
	if n == 1:
		primaria += 1
		n = int(input("¿Posee estudios secundarios?: 1-si / 2-no: "))
		if n == 1:
			secundaria += 1
			n = int(input("¿Posee estudios de carrera técnica?: 1-si / 2-no: "))
			if n == 1:
				tecnicatura += 1
			n = int(input("¿Posee estudios profesionales?: 1-si / 2-no: "))
			if n == 1:
				profesional += 1
				n = int(input("¿Posee estudios de posgrado?: 1-si / 2-no: "))
				if n == 1:
					posgrado += 1
				s = int(input("\nPara agregar otra encuesta presione 1, para salir 0: "))
				if s == 0:
					salir = False	
			else:
				s = int(input("\nPara agregar otra encuesta presione 1, para salir 0: "))
				if s == 0:
					salir = False	
		else:
			s = int(input("\nPara agregar otra encuesta presione 1, para salir 0: "))
			if s == 0:
				salir = False				
	else:
		s = int(input("\nPara agregar otra encuesta presione 1, para salir 0: "))
		if s == 0:
			salir = False	

print("\n\n#Valores diarios:\nPersonas encuestadas: ", persona, "\nPrimario completo: ", primaria*100/persona, "%\nSecundario completo: ", secundaria*100/persona, "%\nTécnicatura completa: ", tecnicatura*100/persona, "%\nCarrera profesional: ", profesional*100/persona, "%\nCarrera posgrado: ", posgrado*100/persona, "%")
