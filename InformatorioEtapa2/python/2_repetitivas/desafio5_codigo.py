contador_m = 0
contador_b = 0
vehiculos = 0
ingreso = 0

while ingreso == 0:
	codigo = str(input("\nIngrese código de monitoreo con formato XXX00000: "))
	vehiculos += 1
	print(codigo)
	if codigo[6] == '1':
		contador_b = contador_b + 1
	if codigo[7] == '1':
		contador_m += 1
	ingreso = int(input("\nSeleccione 0 para agregar código, o presione 1 para salir: "))
else:
	print("\n\nInforme:")
	pr = contador_m*100/vehiculos
	print(vehiculos, "Vehículos informados")
	print(contador_b, "Vehículos tiraron basura")
	print(pr, "% de los vehículos fueron multados")		

	