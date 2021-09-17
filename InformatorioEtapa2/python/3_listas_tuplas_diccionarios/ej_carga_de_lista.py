

personas = list()

while True:
	nombre = input("\nIngrese el nombre del alumno: ")
	sexo = input("Ingrese sexo M o F: ")
	edad = int(input("Ingrese edad: "))
	alumno = [nombre,sexo,edad]
	personas.append(alumno)

	seguir = input("\n¿Desea cargar otro alumno? SI/NO: ")

	if seguir.lower() == "no":
		break