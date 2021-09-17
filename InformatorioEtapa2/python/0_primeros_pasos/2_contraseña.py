ctrs = 1234
a = 0
contador = 5

ing_cts = int(input("\n\nIngrese su contraseña: "))
if ing_cts == ctrs:
	print("\nContraseña correcta")
elif ing_cts != ctrs:
	while a < 4:
		a = a + 1
		contador = contador - 1
		print("\nContraseña Inválida, restan", contador, "intentos")
		ing_cts = int(input("Ingrese su contraseña: "))
	print("\n################\nCuenta Bloqueada\n################")