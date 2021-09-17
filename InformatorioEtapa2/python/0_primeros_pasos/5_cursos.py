
turno = int(input("Ingrese (1) para turno tarde; o (2) para turno noche: "))

if turno == 1:
	palabra = (input("\nIngrese su nombre: "))	
	if palabra[0] <= ('m'):
		print('\nCurso A')
	else:
		print('\nCurso B')			
	
elif turno == 2:
	palabra = (input("\nIngrese su nombre: "))
	if palabra[0] <= ('m'):
		print('\nCurso B')
	else:
		print('\nCurso A')
	
else:
	print('\nVuelva a intentar')
