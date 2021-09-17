

sexo = str(input("\nSeleccione el sexo:\nF:Femenino\nM:Masculino\n\nOpción: "))
altura = float(input("Ingrese altura: "))
sexo_upper = sexo.upper()
if sexo_upper == 'M':
	if altura > 1.72:
		print("\nAltura mayor a la media masculina")
	else:
		print("\nAltura menor a la media masculina")
else:
	if altura > 1.65:
		print("\nAltura mayor a la media femenina")
	else:
		print("\nAltura menor a la media femenina")