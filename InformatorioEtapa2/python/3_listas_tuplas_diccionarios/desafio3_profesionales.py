

profesionales = {}


salida = True

while salida == True:
	nombre = str(input("\nIngrese nombre del profesional: "))
	mail = str(input("Ingrese correo electrónico: "))
	profesionales.setdefault(nombre , mail)
	pregunta = int(input("\n# Ingrese 1 Para seguir cargando, 0 Para salir: "))
	if pregunta > 0:
		salida = True
	else:
		salida = False
else:
	print("\nDiccionario:")
	print(profesionales)